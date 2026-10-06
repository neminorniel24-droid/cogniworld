def apply(world):
    world.biomass = (world.biomass + world.surface_water * 0.004).clamp(0.0, 1.0)
