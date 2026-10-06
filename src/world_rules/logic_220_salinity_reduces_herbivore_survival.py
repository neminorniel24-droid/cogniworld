def apply(world):
    world.herbivore = (world.herbivore - world.salinity * 0.002).clamp(0.0, 1.0)
