def apply(world):
    world.pathogen_load = (world.pathogen_load + 0.002 * world.vegetation * (1.0 - world.biodiversity)).clamp(0.0, 1.0)
