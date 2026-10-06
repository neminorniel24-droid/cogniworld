def apply(world):
    world.biomass = (world.biomass - world.salinity * 0.003).clamp(0.0, 1.0)
