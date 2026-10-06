def apply(world):
    world.temperature = (world.temperature - world.carbon_storage * 0.001).clamp(0.0, 1.0)
