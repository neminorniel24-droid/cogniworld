def apply(world):
    world.erosion = (world.erosion * (1.0 - 0.15 * world.root_density)).clamp(0.0, 1.0)
