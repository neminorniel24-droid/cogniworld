def apply(world):
    world.flowers = (world.flowers + world.predator * 0.001).clamp(0.0, 1.0)
