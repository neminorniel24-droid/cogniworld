def apply(world):
    world.soil_moisture = (world.soil_moisture + 0.01 * world.surface_water).clamp(0.0, 1.0)
