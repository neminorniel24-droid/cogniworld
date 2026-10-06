def apply(world):
    world.pathogen_load = (world.pathogen_load * (1.0 - 0.10 * world.biodiversity)).clamp(0.0, 1.0)
