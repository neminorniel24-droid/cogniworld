def apply(world):
    world.nutrients = (world.nutrients - world.algae * 0.005).clamp(0.0, 1.0)
