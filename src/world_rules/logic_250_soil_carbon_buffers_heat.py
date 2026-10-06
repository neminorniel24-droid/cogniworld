def apply(world):
    world.temperature = (world.temperature - world.soil_carbon * 0.002).clamp(0.0, 1.0)
