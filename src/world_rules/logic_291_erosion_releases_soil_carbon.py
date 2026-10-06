def apply(world):
    world.soil_carbon = (world.soil_carbon - world.erosion * 0.002).clamp(0.0, 1.0)
