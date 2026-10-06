def apply(world):
    world.nutrients = (world.nutrients + 0.008 * world.decomposition_rate).clamp(0.0, 1.0)
