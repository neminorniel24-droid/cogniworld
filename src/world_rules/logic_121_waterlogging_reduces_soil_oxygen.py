def apply(world):
    world.oxygen = (world.oxygen * (1.0 - 0.02 * world.soil_moisture)).clamp(0.0, 1.0)
