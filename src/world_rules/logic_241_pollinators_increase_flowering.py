def apply(world):
    world.flowers = (world.flowers + world.pollinators * 0.01).clamp(0.0, 1.0)
