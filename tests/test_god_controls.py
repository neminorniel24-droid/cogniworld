import torch

from genome.agents import Agents
from brain.batched_brain import BatchedBrain
from world.biome import World
from disease.sir import DiseaseModel, SUSCEPTIBLE, INFECTED
from god.controls import GodControls, region_mask

DEVICE = torch.device("cpu")
CONFIG = {
    "mutation_std": 0.05, "start_energy": 100.0,
    "disease_beta": 1.0, "disease_duration": 30, "disease_energy_drain": 0.5,
}
WORLD_CONFIG = {"world_size": 10, "seed": 1, "elevation_scale": 0.1, "moisture_scale": 0.1, "octaves": 2}


def make_all():
    agents = Agents(n_agents=8, world_size=10, start_energy=100.0, device=DEVICE)
    brain = BatchedBrain(8, 8, 4, 4, DEVICE)
    world = World(WORLD_CONFIG, DEVICE)
    disease = DiseaseModel(CONFIG, 10, DEVICE)
    return agents, brain, world, disease


# ---- pause / speed -----------------------------------------------------

def test_pause_and_speed_default_and_update():
    god = GodControls()
    assert god.snapshot() == {"paused": False, "speed": 1.0, "queued_commands": 0}
    god.set_paused(True)
    god.set_speed(3.0)
    s = god.snapshot()
    assert s["paused"] is True and s["speed"] == 3.0


def test_speed_is_clamped_to_a_sane_range():
    god = GodControls()
    god.set_speed(100.0)
    assert god.snapshot()["speed"] == 10.0
    god.set_speed(-5.0)
    assert god.snapshot()["speed"] == 0.1


# ---- region_mask --------------------------------------------------------

def test_region_mask_selects_only_agents_inside_the_box():
    agents, *_ = make_all()
    agents.pos[0] = torch.tensor([2, 2])
    agents.pos[1] = torch.tensor([5, 5])
    mask = region_mask(agents, {"x0": 0, "y0": 0, "x1": 3, "y1": 3}, world_size=10)
    assert bool(mask[0]) and not bool(mask[1])


def test_region_mask_none_selects_everyone():
    agents, *_ = make_all()
    mask = region_mask(agents, None, world_size=10)
    assert torch.all(mask)


def test_region_mask_handles_swapped_corners():
    agents, *_ = make_all()
    agents.pos[0] = torch.tensor([2, 2])
    mask = region_mask(agents, {"x0": 5, "y0": 5, "x1": 0, "y1": 0}, world_size=10)
    assert bool(mask[0])  # box normalizes even though x1/y1 < x0/y0


# ---- kill ----------------------------------------------------------------

def test_kill_by_region():
    agents, brain, world, disease = make_all()
    agents.pos[:4] = torch.tensor([1, 1])
    agents.pos[4:] = torch.tensor([9, 9])
    god = GodControls()
    god.queue("kill", region={"x0": 0, "y0": 0, "x1": 3, "y1": 3})
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert not torch.any(agents.alive[:4])
    assert torch.all(agents.alive[4:])
    assert "killed 4" in events[0]


def test_kill_by_ids_ignores_out_of_range():
    agents, brain, world, disease = make_all()
    god = GodControls()
    god.queue("kill", ids=[0, 2, 999, -1])
    god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert not agents.alive[0] and not agents.alive[2]
    assert torch.all(agents.alive[[1, 3, 4, 5, 6, 7]])


def test_kill_zeroes_energy_of_killed_agents():
    agents, brain, world, disease = make_all()
    god = GodControls()
    god.queue("kill", ids=[0])
    god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert agents.energy[0].item() == 0.0


# ---- spawn -----------------------------------------------------------

def test_spawn_fills_dead_slots_and_no_more():
    agents, brain, world, disease = make_all()
    agents.alive[:3] = False
    god = GodControls()
    god.queue("spawn", n=2)
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert int(agents.alive.sum()) == 7  # 5 already alive + 2 revived
    assert "spawned 2" in events[0]


def test_spawn_caps_at_available_dead_slots_and_says_so():
    agents, brain, world, disease = make_all()
    agents.alive[0] = False
    god = GodControls()
    god.queue("spawn", n=10)
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert int(agents.alive.sum()) == 8
    assert "spawned 1" in events[0] and "fixed-size" in events[0]


def test_spawn_resets_scarcity_and_disease_state():
    agents, brain, world, disease = make_all()
    agents.alive[0] = False
    agents.ticks_since_food[0] = 500
    agents.infection[0] = INFECTED
    god = GodControls()
    god.queue("spawn", n=1)
    god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert agents.ticks_since_food[0].item() == 0
    assert agents.infection[0].item() == SUSCEPTIBLE


def test_spawn_when_nobody_dead_does_nothing():
    agents, brain, world, disease = make_all()
    god = GodControls()
    god.queue("spawn", n=5)
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert int(agents.alive.sum()) == 8
    assert "spawned 0" in events[0]


# ---- famine / feast ----------------------------------------------------

def test_famine_zeroes_food_in_region_only():
    agents, brain, world, disease = make_all()
    world.food[:, :] = 1.0
    god = GodControls()
    god.queue("famine", region={"x0": 0, "y0": 0, "x1": 4, "y1": 4})
    god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert torch.all(world.food[0:5, 0:5] == 0.0)
    assert torch.all(world.food[5:, 5:] == 1.0)


def test_global_famine_zeroes_everything():
    agents, brain, world, disease = make_all()
    world.food[:, :] = 1.0
    god = GodControls()
    god.queue("famine")
    god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert torch.all(world.food == 0.0)


def test_feast_fills_region_to_cap():
    agents, brain, world, disease = make_all()
    world.food[:, :] = 0.0
    god = GodControls()
    god.queue("feast", region={"x0": 0, "y0": 0, "x1": 2, "y1": 2})
    god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert torch.all(world.food[0:3, 0:3] == 1.0)
    assert torch.all(world.food[3:, 3:] == 0.0)


# ---- seed_disease -------------------------------------------------------

def test_seed_disease_infects_requested_count():
    agents, brain, world, disease = make_all()
    god = GodControls()
    god.queue("seed_disease", n=3)
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert int((agents.infection == INFECTED).sum()) == 3
    assert "seeded disease in 3" in events[0]


# ---- misc -----------------------------------------------------------

def test_queue_is_drained_and_applied_in_order():
    agents, brain, world, disease = make_all()
    god = GodControls()
    god.queue("kill", ids=[0])
    god.queue("spawn", n=1)
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert len(events) == 2
    assert god.snapshot()["queued_commands"] == 0
    assert bool(agents.alive[0])  # killed, then immediately respawned by the queued spawn


def test_unknown_command_is_reported_not_raised():
    agents, brain, world, disease = make_all()
    god = GodControls()
    god.queue("nuke_everything")
    events = god.apply(agents, world, brain, disease, CONFIG, DEVICE)
    assert "unknown command" in events[0]
