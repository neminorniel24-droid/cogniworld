def apply(world):
    world.salinity = (world.salinity + world.evaporation * 0.01).clamp(0.0, 1.0)
