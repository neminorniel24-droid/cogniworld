def apply(world):
    world.soil_moisture = (world.soil_moisture - world.sediment * 0.005).clamp(0.0, 1.0)
