def apply(world):
    world.erosion = (world.erosion - world.soil_carbon * 0.001).clamp(0.0, 1.0)
