def apply(world):
    world.pathogen_load = (world.pathogen_load + world.algae * 0.002).clamp(0.0, 1.0)
