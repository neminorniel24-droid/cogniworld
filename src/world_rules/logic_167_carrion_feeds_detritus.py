def apply(world):
    world.detritus = (world.detritus + 0.005 * world.carrion).clamp(0.0, 1.0)
