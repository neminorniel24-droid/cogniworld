def apply(world):
    world.evaporation = (world.evaporation * (1.0 - 0.5 * world.ice)).clamp(0.0, 1.0)
