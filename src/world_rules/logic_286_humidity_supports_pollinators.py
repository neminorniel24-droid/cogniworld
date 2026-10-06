def apply(world):
    world.pollinators = (world.pollinators + world.humidity * 0.001).clamp(0.0, 1.0)
