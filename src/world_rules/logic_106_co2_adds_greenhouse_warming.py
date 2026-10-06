def apply(world):
    world.temperature_target = (world.temperature_target + 0.004 * world.co2).clamp(0.0, 1.0)
