def apply(world):
    world.temperature_target = (world.temperature_target * (1.0 - 0.01 * world.surface_water) + 0.005 * world.surface_water).clamp(0.0, 1.0)
