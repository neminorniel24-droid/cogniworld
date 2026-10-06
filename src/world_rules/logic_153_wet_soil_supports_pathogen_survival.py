def apply(world):
    world.pathogen_load = (world.pathogen_load + 0.003 * world.soil_moisture).clamp(0.0, 1.0)
