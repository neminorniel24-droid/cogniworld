def apply(world):
    world.humidity = (world.humidity + 0.004 * world.soil_moisture).clamp(0.0, 1.0)
