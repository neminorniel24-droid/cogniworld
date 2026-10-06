def apply(world):
    world.carbon_storage = (world.carbon_storage + 0.01 * world.biomass).clamp(0.0, 1.0)
