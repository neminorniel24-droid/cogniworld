def apply(world):
    world.temperature = (world.temperature - world.surface_ice * 0.01).clamp(0.0, 1.0)
