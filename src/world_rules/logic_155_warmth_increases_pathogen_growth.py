def apply(world):
    world.pathogen_load = (world.pathogen_load + 0.005 * world.temperature).clamp(0.0, 1.0)
