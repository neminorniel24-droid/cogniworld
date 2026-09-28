import torch

from genome.agents import Agents
from brain.batched_brain import BatchedBrain
from evolution.loop import reproduce

DEVICE = torch.device("cpu")

CONFIG = {
    "reproduce_threshold": 150.0,
    "reproduce_cost": 80.0,
    "mutation_std": 0.05,
    "start_energy": 100.0,
}


def make_pop(n=6, n_sensors=8, hidden=4, n_actions=4, world_size=10):
    agents = Agents(n_agents=n, world_size=world_size, start_energy=100.0, device=DEVICE)
    brain = BatchedBrain(n, n_sensors, hidden, n_actions, DEVICE)
    return agents, brain


def test_no_op_when_nobody_dead():
    agents, brain = make_pop()
    w1_before = brain.W1.clone()
    reproduce(agents, brain, CONFIG, DEVICE)
    assert torch.equal(brain.W1, w1_before)  # nothing should change


def test_sexual_path_respawns_dead_slot_with_two_eligible_parents():
    agents, brain = make_pop(n=6)
    agents.alive[0] = False           # one dead slot to fill
    agents.energy[1] = 200.0          # eligible parent A
    agents.energy[2] = 180.0          # eligible parent B
    agents.energy[3:] = 10.0          # not eligible (below threshold)

    reproduce(agents, brain, CONFIG, DEVICE)

    assert bool(agents.alive[0])
    assert agents.energy[0].item() == CONFIG["start_energy"]
    # both eligible parents should have paid half the reproduce cost
    # (they're the only two eligible, so with n=1 dead slot they're both used)
    assert agents.energy[1].item() == 200.0 - CONFIG["reproduce_cost"] / 2
    assert agents.energy[2].item() == 180.0 - CONFIG["reproduce_cost"] / 2


def test_asexual_fallback_when_fewer_than_two_eligible():
    # exactly one other alive agent, so it's deterministically the only
    # possible parent -- no randomness in which agent gets sampled
    agents, brain = make_pop(n=2)
    agents.alive[0] = False
    agents.energy[1] = 200.0  # sole eligible parent

    parent_w1_before = brain.W1[1].clone()
    parent_energy_before = agents.energy[1].item()

    reproduce(agents, brain, CONFIG, DEVICE)

    assert bool(agents.alive[0])
    assert agents.energy[0].item() == CONFIG["start_energy"]
    # asexual fallback costs no energy
    assert agents.energy[1].item() == parent_energy_before
    # child brain should be close to (mutated copy of) the sole parent
    assert torch.allclose(brain.W1[0], parent_w1_before, atol=1.0)


def test_total_extinction_does_not_crash():
    agents, brain = make_pop(n=3)
    agents.alive[:] = False
    reproduce(agents, brain, CONFIG, DEVICE)  # should just no-op, not raise
    assert not torch.any(agents.alive)


def test_respawned_agent_starts_with_fresh_scarcity_counter():
    agents, brain = make_pop(n=2)
    agents.alive[0] = False
    agents.ticks_since_food[0] = 99  # dead agent was deep in a starvation streak
    agents.energy[1] = 100.0
    reproduce(agents, brain, CONFIG, DEVICE)
    assert bool(agents.alive[0])
    assert agents.ticks_since_food[0].item() == 0
