def apply(world):
    melt = world.surface_ice * world.temperature * (1.0 - world.cloud).clamp(0.0, 1.0) * 0.01
    world.surface_ice = (world.surface_ice - melt).clamp(0.0, 1.0)
