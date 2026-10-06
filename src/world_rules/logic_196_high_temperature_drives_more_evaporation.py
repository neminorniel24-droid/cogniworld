def apply(world):
    world.evaporation = (world.evaporation + 0.006 * world.temperature).clamp(0.0, 1.0)
