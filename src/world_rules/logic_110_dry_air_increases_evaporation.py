def apply(world):
    world.evaporation = (world.evaporation + 0.005 * (1.0 - world.humidity)).clamp(0.0, 1.0)
