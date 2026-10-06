def apply(world):
    world.surface_ice = (world.surface_ice + (0.2 - world.temperature).clamp(0.0, 0.2) * 0.1).clamp(0.0, 1.0)
