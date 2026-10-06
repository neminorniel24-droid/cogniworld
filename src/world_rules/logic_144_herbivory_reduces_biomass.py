def apply(world):
    world.biomass = (world.biomass - 0.008 * world.herbivore).clamp(0.0, 1.0)
