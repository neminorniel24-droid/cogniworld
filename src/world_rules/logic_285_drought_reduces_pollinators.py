def apply(world):
    world.pollinators = (world.pollinators - (1.0 - world.soil_moisture).clamp(0.0, 1.0) * 0.001).clamp(0.0, 1.0)
