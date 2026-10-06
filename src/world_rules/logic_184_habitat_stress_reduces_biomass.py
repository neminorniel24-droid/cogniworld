def apply(world):
    world.biomass = (world.biomass - 0.004 * world.habitat_stress).clamp(0.0, 1.0)
