def apply(world):
    melt = world.surface_ice * world.temperature * 0.04
    world.surface_ice = (world.surface_ice - melt).clamp(0.0, 1.0)
    world.surface_water = (world.surface_water + melt).clamp(0.0, 1.0)
