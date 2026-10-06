def apply(world):
    world.temperature_target = (world.temperature_target - 0.004 * world.cloud * world.rain).clamp(0.0, 1.0)
