"""
Migration pressure (Phase 2): agents stuck too long without food become
more willing to move -- represented as a per-agent discount on move_cost.

This intentionally doesn't change *where* an agent moves (that's still the
brain's job, via its argmax action). It only makes movement cheaper for a
starving agent, which combined with evolved brain behavior (sensing food in
neighbor tiles) should let scarcity-driven wandering emerge from selection
pressure rather than being hand-scripted.
"""
import torch


def compute_move_cost(agents, base_move_cost: float, config: dict) -> torch.Tensor:
    """Per-agent move cost: base cost, discounted for agents that have gone
    config['migration_scarcity_ticks'] or more ticks without eating.

    Returns a [N] tensor -- Agents.act() already accepts move_cost as
    anything broadcastable against self.energy, so no change needed there.
    """
    scarce = agents.ticks_since_food >= config["migration_scarcity_ticks"]
    discount = config["migration_move_discount"]  # e.g. 0.5 = half price
    cost = torch.full_like(agents.energy, base_move_cost)
    cost = torch.where(scarce, cost * discount, cost)
    return cost
