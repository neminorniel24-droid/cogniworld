def apply(world):
    world.oxygen = (world.oxygen - world.algae * 0.002).clamp(0.0, 1.0)
