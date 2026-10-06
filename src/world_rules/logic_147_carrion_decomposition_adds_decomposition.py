def apply(world):
    world.decomposition_rate = (world.decomposition_rate + 0.006 * world.carrion).clamp(0.0, 1.0)
