def apply(world):
    world.organic_matter = (world.organic_matter + world.soil_moisture * 0.01).clamp(0.0, 1.0)
