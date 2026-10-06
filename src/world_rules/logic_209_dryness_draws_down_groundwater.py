def apply(world):
    world.groundwater = (world.groundwater - (1.0 - world.soil_moisture) * 0.003).clamp(0.0, 1.0)
