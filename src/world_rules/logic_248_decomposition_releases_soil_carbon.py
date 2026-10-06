def apply(world):
    world.soil_carbon = (world.soil_carbon - world.decomposition_rate * 0.003).clamp(0.0, 1.0)
