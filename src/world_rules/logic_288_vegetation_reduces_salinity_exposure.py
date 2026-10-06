def apply(world):
    world.salinity = (world.salinity - world.vegetation * 0.001).clamp(0.0, 1.0)
