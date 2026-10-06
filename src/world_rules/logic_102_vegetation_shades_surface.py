def apply(world):
    world.temperature_target = (world.temperature_target - 0.008 * world.vegetation).clamp(0.0, 1.0)
