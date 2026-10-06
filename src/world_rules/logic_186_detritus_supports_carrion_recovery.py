def apply(world):
    world.carrion = (world.carrion + 0.001 * world.detritus).clamp(0.0, 1.0)
