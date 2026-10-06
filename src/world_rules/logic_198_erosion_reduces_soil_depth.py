def apply(world):
    world.soil_depth = (world.soil_depth - 0.01 * world.erosion).clamp(0.0, 1.0)
