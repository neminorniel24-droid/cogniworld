def apply(world):
    world.temperature_target = (world.temperature_target + 0.002 * world.cloud).clamp(0.0, 1.0)
