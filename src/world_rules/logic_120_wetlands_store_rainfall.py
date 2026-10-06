def apply(world):
    world.surface_water = (world.surface_water + 0.01 * world.wetland * world.rain).clamp(0.0, 1.0)
