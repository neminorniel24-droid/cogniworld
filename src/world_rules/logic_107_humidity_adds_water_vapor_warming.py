def apply(world):
    world.temperature_target = (world.temperature_target + 0.003 * world.humidity).clamp(0.0, 1.0)
