"""
Genetic algorithm evolution loop (no backprop needed).

Every N steps:
  1. Find dead agent slots.
  2. Pick parents from the living population, weighted by energy (fitness).
  3. Copy parent's brain into the dead slot with Gaussian mutation.
  4. Respawn the slot at a random position with starting energy.

This keeps population size constant while letting successful genomes spread.
"""
import torch


def reproduce(agents, brain, config: dict, device: torch.device):
    dead_idx = (~agents.alive).nonzero(as_tuple=True)[0]
    alive_idx = agents.alive.nonzero(as_tuple=True)[0]

    if len(dead_idx) == 0 or len(alive_idx) == 0:
        return  # nothing to do (either everyone alive, or total extinction)

    # fitness-weighted parent sampling from the living population
    fitness = agents.energy[alive_idx].clamp(min=1e-3)
    probs = fitness / fitness.sum()
    parent_choice = torch.multinomial(probs, len(dead_idx), replacement=True)
    parent_idx = alive_idx[parent_choice]

    brain.mutate_into(parent_idx, dead_idx, config["mutation_std"])

    # respawn physical state
    agents.pos[dead_idx] = torch.randint(
        0, agents.world_size, (len(dead_idx), 2), device=device
    )
    agents.energy[dead_idx] = config["start_energy"]
    agents.alive[dead_idx] = True
