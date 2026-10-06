def apply(world):
    world.co2 = (world.co2 - world.soil_carbon * 0.002).clamp(0.0, 1.0)
