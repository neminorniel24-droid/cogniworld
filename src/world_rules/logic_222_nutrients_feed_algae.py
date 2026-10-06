def apply(world):
    world.algae = (world.algae + world.nutrients * 0.015).clamp(0.0, 1.0)
