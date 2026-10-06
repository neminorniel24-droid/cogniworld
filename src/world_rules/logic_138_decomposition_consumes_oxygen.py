def apply(world):
    world.oxygen = (world.oxygen - 0.003 * world.decomposition_rate).clamp(0.0, 1.0)
