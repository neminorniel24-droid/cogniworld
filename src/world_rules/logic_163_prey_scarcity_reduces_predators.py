def apply(world):
    world.predator = (world.predator * (0.985 + 0.015 * world.herbivore)).clamp(0.0, 1.0)
