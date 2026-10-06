def apply(world):
    world.carbon_storage = (world.carbon_storage + world.deadwood * 0.01).clamp(0.0, 1.0)
