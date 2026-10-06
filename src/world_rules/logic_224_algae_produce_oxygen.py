def apply(world):
    world.oxygen = (world.oxygen + world.algae * 0.01).clamp(0.0, 1.0)
