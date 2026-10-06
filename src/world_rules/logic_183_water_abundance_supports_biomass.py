def apply(world):
    world.biomass = (world.biomass + 0.004 * world.soil_moisture * (1.0 - world.biomass)).clamp(0.0, 1.0)
