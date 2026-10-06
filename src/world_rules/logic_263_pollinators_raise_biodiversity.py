def apply(world):
    world.biodiversity = (world.biodiversity + world.pollinators * 0.002).clamp(0.0, 1.0)
