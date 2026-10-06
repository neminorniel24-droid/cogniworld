def apply(world):
    world.algae = (world.algae - world.oxygen * 0.001).clamp(0.0, 1.0)
