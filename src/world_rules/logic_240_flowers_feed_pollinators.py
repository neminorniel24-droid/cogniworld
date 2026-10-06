def apply(world):
    world.pollinators = (world.pollinators + world.flowers * 0.02).clamp(0.0, 1.0)
