def apply(world):
    world.methane = (world.methane * (0.99 + 0.01 * world.soil_moisture)).clamp(0.0, 1.0)
