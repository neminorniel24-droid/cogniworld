def apply(world):
    world.vegetation = (world.vegetation * (0.99 + 0.01 * world.nutrients)).clamp(0.0, 1.0)
