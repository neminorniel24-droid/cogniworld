def apply(world):
    world.decomposition_rate = (world.decomposition_rate * (0.99 + 0.02 * world.temperature)).clamp(0.0, 1.0)
