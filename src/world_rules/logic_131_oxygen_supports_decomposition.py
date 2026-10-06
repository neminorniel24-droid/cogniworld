def apply(world):
    world.decomposition_rate = (world.decomposition_rate + 0.01 * world.oxygen).clamp(0.0, 1.0)
