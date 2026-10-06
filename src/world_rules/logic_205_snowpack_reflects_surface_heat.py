def apply(world):
    world.temperature = (world.temperature - world.snowpack * 0.02).clamp(0.0, 1.0)
