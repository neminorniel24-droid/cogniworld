def apply(world):
    world.pollinators = (world.pollinators + world.vegetation * 0.01).clamp(0.0, 1.0)
