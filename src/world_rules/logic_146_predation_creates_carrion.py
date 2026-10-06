def apply(world):
    world.carrion = (world.carrion + 0.004 * world.predator * world.herbivore).clamp(0.0, 1.0)
