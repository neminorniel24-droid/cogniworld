def apply(world):
    world.biomass = (world.biomass - 0.005 * (1.0 - world.soil_moisture)).clamp(0.0, 1.0)
