def apply(world):
    world.root_density = (world.root_density + 0.004 * world.biomass).clamp(0.0, 1.0)
