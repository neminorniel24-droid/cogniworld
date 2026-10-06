def apply(world):
    world.herbivore = (world.herbivore - 0.005 * world.predator).clamp(0.0, 1.0)
