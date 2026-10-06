def apply(world):
    world.salinity = (world.salinity - world.rain * 0.02).clamp(0.0, 1.0)
