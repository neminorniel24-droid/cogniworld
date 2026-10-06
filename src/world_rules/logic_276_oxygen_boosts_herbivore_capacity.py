def apply(world):
    world.herbivore = (world.herbivore + world.oxygen * 0.001).clamp(0.0, 1.0)
