def apply(world):
    world.co2 = (world.co2 + 0.004 * world.decomposition_rate).clamp(0.0, 1.0)
