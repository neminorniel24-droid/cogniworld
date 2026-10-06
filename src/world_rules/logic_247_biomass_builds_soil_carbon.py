def apply(world):
    world.soil_carbon = (world.soil_carbon + world.biomass * 0.01).clamp(0.0, 1.0)
