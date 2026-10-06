def apply(world):
    world.surface_water = (world.surface_water + world.surface_ice * 0.002).clamp(0.0, 1.0)
