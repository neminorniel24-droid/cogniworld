def apply(world):
    world.detritus = (world.detritus - 0.01 * world.decomposition_rate).clamp(0.0, 1.0)
