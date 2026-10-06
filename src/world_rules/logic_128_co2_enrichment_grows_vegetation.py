def apply(world):
    world.vegetation = (world.vegetation + 0.006 * world.co2 * world.photosynthesis_factor).clamp(0.0, 1.0)
