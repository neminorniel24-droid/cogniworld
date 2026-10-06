def apply(world):
    world.biodiversity = (world.biodiversity - world.deadwood * 0.001).clamp(0.0, 1.0)
