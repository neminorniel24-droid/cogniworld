def apply(world):
    world.salinity = (world.salinity - world.surface_water * 0.01).clamp(0.0, 1.0)
