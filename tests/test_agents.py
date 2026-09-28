import torch

from genome.agents import Agents

DEVICE = torch.device("cpu")


class FakeWorld:
    """Minimal stand-in for world.biome.World -- just food/shelter grids."""
    def __init__(self, size):
        self.food = torch.zeros(size, size)
        self.shelter = torch.zeros(size, size)


def test_sense_shape_and_bias_term():
    agents = Agents(n_agents=5, world_size=10, start_energy=100.0, device=DEVICE)
    world = FakeWorld(10)
    sensors = agents.sense(world)
    assert sensors.shape == (5, 8)
    assert torch.all(sensors[:, 7] == 1.0)  # bias term is always 1.0


def test_sense_reads_food_at_agent_position():
    agents = Agents(n_agents=1, world_size=10, start_energy=100.0, device=DEVICE)
    agents.pos[0] = torch.tensor([3, 4])
    world = FakeWorld(10)
    world.food[4, 3] = 0.75  # world.food is indexed [y, x]
    sensors = agents.sense(world)
    assert sensors[0, 0].item() == 0.75


def test_act_moves_eats_and_costs_energy():
    agents = Agents(n_agents=1, world_size=10, start_energy=100.0, device=DEVICE)
    agents.pos[0] = torch.tensor([5, 5])
    world = FakeWorld(10)
    world.food[5, 4] = 1.0  # food to the west (action index 3 -> dx=-1)

    action_logits = torch.zeros(1, 4)
    action_logits[0, 3] = 10.0  # force argmax -> move west

    ate = agents.act(action_logits, world, move_cost=0.5, metabolism_cost=0.2)

    assert agents.pos[0].tolist() == [4, 5]
    assert bool(ate[0])
    # gained 1.0 food * 40 energy, minus move_cost + metabolism_cost
    expected_energy = 100.0 + 1.0 * 40.0 - 0.5 - 0.2
    assert abs(agents.energy[0].item() - expected_energy) < 1e-4


def test_act_kills_agent_at_zero_energy():
    agents = Agents(n_agents=1, world_size=10, start_energy=0.3, device=DEVICE)
    world = FakeWorld(10)
    action_logits = torch.zeros(1, 4)
    agents.act(action_logits, world, move_cost=0.5, metabolism_cost=0.2)
    assert agents.energy[0].item() == 0.0
    assert not bool(agents.alive[0])


def test_energy_clamped_to_max():
    agents = Agents(n_agents=1, world_size=10, start_energy=199.0, device=DEVICE)
    world = FakeWorld(10)
    world.food[:, :] = 1.0  # food everywhere so agent definitely eats
    action_logits = torch.zeros(1, 4)
    agents.act(action_logits, world, move_cost=0.0, metabolism_cost=0.0, max_energy=200.0)
    assert agents.energy[0].item() == 200.0
