def apply(world):
    world.vegetation = (world.vegetation + 0.005 * world.ash * (1.0 - world.vegetation)).clamp(0.0, 1.0)
