def apply(world):
    world.carbon_storage = (world.carbon_storage - 0.004 * world.runoff).clamp(0.0, 1.0)
