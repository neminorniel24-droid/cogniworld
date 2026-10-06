def apply(world):
    world.herbivore = (world.herbivore * (0.99 + 0.01 * world.oxygen)).clamp(0.0, 1.0)
