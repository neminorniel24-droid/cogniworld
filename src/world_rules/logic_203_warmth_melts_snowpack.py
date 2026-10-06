def apply(world):
    melt = world.snowpack * world.temperature * 0.05
    world.snowpack = (world.snowpack - melt).clamp(0.0, 1.0)
    world.surface_water = (world.surface_water + melt).clamp(0.0, 1.0)
