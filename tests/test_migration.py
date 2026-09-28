import torch

from genome.agents import Agents
from migration.pressure import compute_move_cost

DEVICE = torch.device("cpu")

CONFIG = {
    "migration_scarcity_ticks": 20,
    "migration_move_discount": 0.5,
}


def test_well_fed_agent_pays_full_move_cost():
    agents = Agents(n_agents=2, world_size=10, start_energy=100.0, device=DEVICE)
    agents.ticks_since_food[:] = 0
    cost = compute_move_cost(agents, base_move_cost=0.5, config=CONFIG)
    assert torch.all(cost == 0.5)


def test_scarce_agent_gets_discounted_move_cost():
    agents = Agents(n_agents=2, world_size=10, start_energy=100.0, device=DEVICE)
    agents.ticks_since_food[0] = 25   # over threshold -> discounted
    agents.ticks_since_food[1] = 5    # under threshold -> full price
    cost = compute_move_cost(agents, base_move_cost=0.5, config=CONFIG)
    assert cost[0].item() == 0.25
    assert cost[1].item() == 0.5


def test_threshold_is_inclusive():
    agents = Agents(n_agents=1, world_size=10, start_energy=100.0, device=DEVICE)
    agents.ticks_since_food[0] = CONFIG["migration_scarcity_ticks"]  # exactly at threshold
    cost = compute_move_cost(agents, base_move_cost=1.0, config=CONFIG)
    assert cost[0].item() == 0.5  # discount already applies at the threshold tick


def test_output_is_usable_directly_by_agents_act():
    """compute_move_cost's output should broadcast fine as Agents.act's
    move_cost argument -- this is what actually matters end-to-end."""
    agents = Agents(n_agents=3, world_size=10, start_energy=100.0, device=DEVICE)
    agents.ticks_since_food[:] = torch.tensor([0, 25, 25])

    class FakeWorld:
        def __init__(self, size):
            self.food = torch.zeros(size, size)
            self.shelter = torch.zeros(size, size)

    world = FakeWorld(10)
    move_cost = compute_move_cost(agents, base_move_cost=1.0, config=CONFIG)
    energy_before = agents.energy.clone()
    action_logits = torch.zeros(3, 4)
    agents.act(action_logits, world, move_cost=move_cost, metabolism_cost=0.0)

    # agent 0 (not scarce) should have paid more energy than agents 1/2 (scarce)
    spent = energy_before - agents.energy
    assert spent[0].item() > spent[1].item()
    assert spent[1].item() == spent[2].item()
