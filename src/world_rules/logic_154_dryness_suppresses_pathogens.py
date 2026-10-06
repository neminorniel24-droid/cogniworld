def apply(world):
    world.pathogen_load = (world.pathogen_load * (0.985 + 0.015 * world.soil_moisture)).clamp(0.0, 1.0)
