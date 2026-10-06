def apply(world):
    world.flowers = (world.flowers - world.herbivore * 0.002).clamp(0.0, 1.0)
