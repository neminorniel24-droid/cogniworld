def apply(world):
    world.surface_water = (world.surface_water + 0.02 * world.runoff).clamp(0.0, 1.0)
