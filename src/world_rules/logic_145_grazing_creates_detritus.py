def apply(world):
    world.detritus = (world.detritus + 0.003 * world.herbivore).clamp(0.0, 1.0)
