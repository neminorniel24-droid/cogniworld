"""
Phase 3: SIR disease model, density-driven.

Each agent is Susceptible (0), Infected (1) or Recovered (2, immune).

Per tick (DiseaseModel.step):
  1. Count infected agents per tile, then sum over each tile's 3x3
     neighborhood -- this is each agent's "exposure".
  2. A susceptible agent catches the disease with probability
     1 - (1 - beta) ** exposure, so crowded areas spread it much faster
     than sparse ones (density-driven outbreaks, no per-agent loops).
  3. Infected agents lose extra energy each tick, and recover (gaining
     immunity) after `infection_duration` ticks. Sick agents that run out
     of energy die like any other death; reproduce() then respawns the slot
     as a fresh susceptible agent, which is what lets the disease persist.

Everything is batched tensor ops, same as the rest of the sim.
"""
import torch
import torch.nn.functional as F

SUSCEPTIBLE, INFECTED, RECOVERED = 0, 1, 2


class DiseaseModel:
    def __init__(self, config: dict, world_size: int, device: torch.device):
        self.beta = config["disease_beta"]
        self.duration = config["disease_duration"]
        self.drain = config["disease_energy_drain"]
        self.world_size = world_size
        self.device = device
        self._kernel = torch.ones(1, 1, 3, 3, device=device)

    def seed(self, agents, n: int) -> int:
        """Infect up to n random living susceptible agents. Returns how many."""
        candidates = (agents.alive & (agents.infection == SUSCEPTIBLE)).nonzero(as_tuple=True)[0]
        if len(candidates) == 0 or n <= 0:
            return 0
        pick = candidates[torch.randperm(len(candidates), device=self.device)[:n]]
        agents.infection[pick] = INFECTED
        agents.infection_timer[pick] = 0
        return len(pick)

    def _exposure(self, agents, infected: torch.Tensor) -> torch.Tensor:
        """Per-agent count of infected agents in its tile + 8 neighboring tiles."""
        w = self.world_size
        flat = agents.pos[:, 1] * w + agents.pos[:, 0]
        per_tile = torch.bincount(flat[infected], minlength=w * w).view(1, 1, w, w).float()
        nearby = F.conv2d(per_tile, self._kernel, padding=1)[0, 0]  # [w, w]
        return nearby[agents.pos[:, 1], agents.pos[:, 0]]

    def step(self, agents):
        infected = agents.alive & (agents.infection == INFECTED)

        # transmission, based on who was infected at the start of the tick
        exposure = self._exposure(agents, infected)
        p_catch = 1.0 - (1.0 - self.beta) ** exposure
        newly_infected = (
            agents.alive
            & (agents.infection == SUSCEPTIBLE)
            & (torch.rand_like(p_catch) < p_catch)
        )

        # progression for the already-infected
        agents.infection_timer = torch.where(
            infected, agents.infection_timer + 1, agents.infection_timer
        )
        agents.energy = torch.where(infected, agents.energy - self.drain, agents.energy)
        agents.energy.clamp_(min=0)
        agents.alive &= agents.energy > 0  # the disease can kill

        recovered = infected & agents.alive & (agents.infection_timer >= self.duration)
        agents.infection[recovered] = RECOVERED

        agents.infection[newly_infected] = INFECTED
        agents.infection_timer[newly_infected] = 0

    def counts(self, agents) -> dict:
        alive = agents.alive
        return {
            "susceptible": int((alive & (agents.infection == SUSCEPTIBLE)).sum().item()),
            "infected": int((alive & (agents.infection == INFECTED)).sum().item()),
            "recovered": int((alive & (agents.infection == RECOVERED)).sum().item()),
        }
