def apply(world):
    world.pathogen_load = (world.pathogen_load * (1.0 - 0.12 * world.rain)).clamp(0.0, 1.0)
