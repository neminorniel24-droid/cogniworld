def apply(world):
    world.predator = (world.predator - world.salinity * 0.0015).clamp(0.0, 1.0)
