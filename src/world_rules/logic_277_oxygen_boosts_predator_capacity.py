def apply(world):
    world.predator = (world.predator + world.oxygen * 0.001).clamp(0.0, 1.0)
