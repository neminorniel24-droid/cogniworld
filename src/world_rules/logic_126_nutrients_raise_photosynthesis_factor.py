def apply(world):
    world.photosynthesis_factor = (world.photosynthesis_factor + 0.02 * world.nutrients).clamp(0.0, 1.0)
