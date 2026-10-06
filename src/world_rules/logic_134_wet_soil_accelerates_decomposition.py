def apply(world):
    world.decomposition_rate = (world.decomposition_rate + 0.008 * world.soil_moisture).clamp(0.0, 1.0)
