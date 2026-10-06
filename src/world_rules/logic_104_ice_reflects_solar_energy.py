def apply(world):
    world.temperature_target = (world.temperature_target - 0.012 * world.ice).clamp(0.0, 1.0)
