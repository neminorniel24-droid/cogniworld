def apply(world):
    world.pathogen_load = (world.pathogen_load - world.predator * 0.001).clamp(0.0, 1.0)
