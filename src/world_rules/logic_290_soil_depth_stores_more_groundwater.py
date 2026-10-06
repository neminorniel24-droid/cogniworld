def apply(world):
    world.groundwater = (world.groundwater + world.soil_depth * 0.002).clamp(0.0, 1.0)
