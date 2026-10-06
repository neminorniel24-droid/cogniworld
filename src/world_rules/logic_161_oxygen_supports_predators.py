def apply(world):
    world.predator = (world.predator + 0.003 * world.oxygen).clamp(0.0, 1.0)
