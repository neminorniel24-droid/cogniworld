"""
Evolution loop: two-parent (sexual) reproduction, with an asexual fallback
for early on when too few agents have enough energy to mate.

Every N steps:
  1. Find dead agent slots.
  2. Eligible parents = alive agents with energy above reproduce_threshold.
     - If >= 2 eligible: pick two distinct-ish parents per dead slot,
       fitness-weighted by energy, and crossover their brains (see
       BatchedBrain.crossover_into). Both parents pay reproduce_cost,
       split between them, as the "cost" of producing offspring.
     - Otherwise: fall back to the old asexual path (single parent +
       mutation, no energy cost) so the population doesn't stall out
       before anyone has built up enough energy to mate.
  3. Respawn the dead slot at a random position with starting energy.

This keeps population size constant while letting successful genomes
(now recombined, not just cloned) spread through the population.
"""
import torch


def reproduce(agents, brain, config: dict, device: torch.device):
    dead_idx = (~agents.alive).nonzero(as_tuple=True)[0]
    alive_idx = agents.alive.nonzero(as_tuple=True)[0]

    if len(dead_idx) == 0 or len(alive_idx) == 0:
        return  # nothing to do (either everyone alive, or total extinction)

    n_dead = len(dead_idx)
    eligible_mask = agents.energy[alive_idx] > config["reproduce_threshold"]
    eligible_idx = alive_idx[eligible_mask]

    if len(eligible_idx) >= 2:
        fitness = agents.energy[eligible_idx].clamp(min=1e-3)
        probs = fitness / fitness.sum()

        parent_a_choice = torch.multinomial(probs, n_dead, replacement=True)
        parent_b_choice = torch.multinomial(probs, n_dead, replacement=True)

        # avoid a parent mating with itself: resample colliding pairs until
        # none remain (bounded so we can't loop forever). A single resample
        # attempt isn't enough -- it can re-collide by chance, and a
        # self-paired agent would get charged reproduce_cost twice (once as
        # "parent A", once as "parent B") instead of once. With an eligible
        # pool of >= 2 (guaranteed by the branch above), 20 attempts drives
        # the residual collision chance low enough to ignore in practice.
        for _ in range(20):
            self_paired = parent_a_choice == parent_b_choice
            if not self_paired.any():
                break
            parent_b_choice[self_paired] = torch.multinomial(
                probs, int(self_paired.sum()), replacement=True
            )

        parent_a_idx = eligible_idx[parent_a_choice]
        parent_b_idx = eligible_idx[parent_b_choice]

        brain.crossover_into(parent_a_idx, parent_b_idx, dead_idx, config["mutation_std"])

        # both parents pay half the reproduce cost -- can, rarely, kill a
        # low-energy parent right after it mates. That death just gets
        # picked up on the next reproduce() call, same as any other death.
        half_cost = config["reproduce_cost"] * 0.5
        agents.energy[parent_a_idx] -= half_cost
        agents.energy[parent_b_idx] -= half_cost
        agents.energy.clamp_(min=0)
        agents.alive &= agents.energy > 0
    else:
        # not enough energy-rich agents yet to mate -- clone-and-mutate
        # the best of what's alive so the population can recover
        fitness = agents.energy[alive_idx].clamp(min=1e-3)
        probs = fitness / fitness.sum()
        parent_choice = torch.multinomial(probs, n_dead, replacement=True)
        parent_idx = alive_idx[parent_choice]
        brain.mutate_into(parent_idx, dead_idx, config["mutation_std"])

    # respawn physical state for the offspring
    agents.pos[dead_idx] = torch.randint(
        0, agents.world_size, (n_dead, 2), device=device
    )
    agents.energy[dead_idx] = config["start_energy"]
    agents.alive[dead_idx] = True
    agents.ticks_since_food[dead_idx] = 0  # newborns don't inherit the dead agent's scarcity streak
    agents.infection[dead_idx] = 0         # ...or its disease: offspring are born susceptible
    agents.infection_timer[dead_idx] = 0
