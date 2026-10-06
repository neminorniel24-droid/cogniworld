def apply(world):
    world.predator = (world.predator + 0.004 * world.herbivore).clamp(0.0, 1.0)
