def apply(world):
    world.oxygen = (world.oxygen + 0.008 * world.biomass * world.photosynthesis_factor).clamp(0.0, 1.0)
