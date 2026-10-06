def apply(world):
    world.herbivore = (world.herbivore + world.flowers * 0.003).clamp(0.0, 1.0)
