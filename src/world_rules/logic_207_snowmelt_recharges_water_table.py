def apply(world):
    world.groundwater = (world.groundwater + world.snowpack * 0.01).clamp(0.0, 1.0)
