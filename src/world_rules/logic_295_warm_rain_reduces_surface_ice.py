def apply(world):
    melt = world.rain * world.temperature * 0.02
    world.surface_ice = (world.surface_ice - melt).clamp(0.0, 1.0)
