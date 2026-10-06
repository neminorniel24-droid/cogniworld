def apply(world):
    world.nutrients = (world.nutrients - 0.02 * world.erosion).clamp(0.0, 1.0)
