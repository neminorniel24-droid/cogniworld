import torch

from genome.agents import Agents
from disease.sir import DiseaseModel, SUSCEPTIBLE, INFECTED, RECOVERED

DEVICE = torch.device("cpu")
WORLD = 20


def make(n, beta=1.0, duration=3, drain=1.0):
    agents = Agents(n_agents=n, world_size=WORLD, start_energy=100.0, device=DEVICE)
    config = {"disease_beta": beta, "disease_duration": duration, "disease_energy_drain": drain}
    return agents, DiseaseModel(config, WORLD, DEVICE)


def place(agents, idx, x, y):
    agents.pos[idx] = torch.tensor([x, y])


def test_seed_infects_requested_number_of_living_agents():
    agents, disease = make(10)
    agents.alive[:3] = False
    assert disease.seed(agents, 4) == 4
    assert int((agents.infection == INFECTED).sum()) == 4
    assert not torch.any((agents.infection == INFECTED) & ~agents.alive)


def test_seed_caps_at_available_candidates():
    agents, disease = make(3)
    assert disease.seed(agents, 50) == 3


def test_no_infected_means_no_new_infections():
    agents, disease = make(10, beta=1.0)
    disease.step(agents)
    assert int((agents.infection != SUSCEPTIBLE).sum()) == 0


def test_transmission_same_tile_and_adjacent_but_not_two_away():
    agents, disease = make(4, beta=1.0)
    place(agents, 0, 5, 5)   # infected source
    place(agents, 1, 5, 5)   # same tile
    place(agents, 2, 6, 6)   # diagonal neighbor
    place(agents, 3, 8, 5)   # 3 tiles away
    agents.infection[0] = INFECTED
    disease.step(agents)
    assert agents.infection[1].item() == INFECTED
    assert agents.infection[2].item() == INFECTED
    assert agents.infection[3].item() == SUSCEPTIBLE


def test_zero_beta_never_transmits():
    agents, disease = make(4, beta=0.0)
    place(agents, torch.arange(4), 5, 5)
    agents.infection[0] = INFECTED
    for _ in range(10):
        disease.step(agents)
    # the source recovers, but nobody else ever catches it
    assert torch.all(agents.infection[1:] == SUSCEPTIBLE)


def test_infected_recover_after_duration_and_become_immune():
    agents, disease = make(2, beta=1.0, duration=3, drain=0.0)
    place(agents, torch.arange(2), 5, 5)
    agents.infection[0] = INFECTED
    for _ in range(3):
        disease.step(agents)
    assert agents.infection[0].item() == RECOVERED
    # immune: an active infected neighbor must not reinfect it
    agents.infection[1] = INFECTED
    agents.infection_timer[1] = 0
    disease.step(agents)
    assert agents.infection[0].item() == RECOVERED


def test_infection_drains_only_infected_agents_energy():
    agents, disease = make(2, beta=0.0, drain=5.0)
    place(agents, 0, 0, 0)
    place(agents, 1, 15, 15)
    agents.infection[0] = INFECTED
    disease.step(agents)
    assert agents.energy[0].item() == 95.0
    assert agents.energy[1].item() == 100.0


def test_disease_can_kill_a_weak_infected_agent():
    agents, disease = make(1, beta=0.0, drain=5.0)
    agents.energy[0] = 3.0
    agents.infection[0] = INFECTED
    disease.step(agents)
    assert not bool(agents.alive[0])
    assert agents.energy[0].item() == 0.0


def test_dead_agents_do_not_transmit():
    agents, disease = make(2, beta=1.0)
    place(agents, torch.arange(2), 5, 5)
    agents.infection[0] = INFECTED
    agents.alive[0] = False
    disease.step(agents)
    assert agents.infection[1].item() == SUSCEPTIBLE


def test_crowding_speeds_up_spread():
    """Density-driven: same disease, same source, more infected neighbors
    in the area => more susceptibles caught in one tick."""
    torch.manual_seed(0)

    def caught(n_infected_around):
        agents, disease = make(200, beta=0.2)
        place(agents, torch.arange(200), 5, 5)          # everyone on one tile...
        agents.infection[:n_infected_around] = INFECTED  # ...some already sick
        disease.step(agents)
        return int((agents.infection[n_infected_around:] == INFECTED).sum())

    assert caught(1) < caught(10)


def test_counts_only_include_living_agents():
    agents, disease = make(6)
    agents.infection[:2] = INFECTED
    agents.infection[2:3] = RECOVERED
    agents.alive[0] = False
    assert disease.counts(agents) == {"susceptible": 3, "infected": 1, "recovered": 1}
