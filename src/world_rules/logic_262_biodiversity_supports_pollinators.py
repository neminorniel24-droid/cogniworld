def apply(world):
    world.pollinators = (world.pollinators + world.biodiversity * 0.004).clamp(0.0, 1.0)
