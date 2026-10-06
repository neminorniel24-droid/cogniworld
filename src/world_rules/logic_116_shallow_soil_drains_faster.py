def apply(world):
    world.soil_moisture = (world.soil_moisture * (0.98 + 0.02 * world.soil_depth)).clamp(0.0, 1.0)
