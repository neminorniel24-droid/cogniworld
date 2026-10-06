def apply(world):
    world.pathogen_load = (world.pathogen_load + 0.004 * world.habitat_stress).clamp(0.0, 1.0)
