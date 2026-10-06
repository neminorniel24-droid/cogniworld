def apply(world):
    world.carbon_storage = (world.carbon_storage - 0.006 * (1.0 - world.soil_moisture)).clamp(0.0, 1.0)
