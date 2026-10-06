def apply(world):
    world.methane = (world.methane * (1.0 - 0.05 * world.oxygen)).clamp(0.0, 1.0)
