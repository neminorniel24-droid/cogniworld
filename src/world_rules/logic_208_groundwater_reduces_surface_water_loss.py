def apply(world):
    world.surface_water = (world.surface_water + world.groundwater * 0.01).clamp(0.0, 1.0)
