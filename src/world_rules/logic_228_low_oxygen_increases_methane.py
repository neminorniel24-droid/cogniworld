def apply(world):
    world.methane = (world.methane + (1.0 - world.oxygen).clamp(0.0, 1.0) * 0.004).clamp(0.0, 1.0)
