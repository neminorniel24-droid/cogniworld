def apply(world):
    world.vegetation = (world.vegetation - world.salinity * 0.004).clamp(0.0, 1.0)
