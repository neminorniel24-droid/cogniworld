def apply(world):
    world.temperature_target = (world.temperature_target - 0.002 * world.carbon_storage).clamp(0.0, 1.0)
