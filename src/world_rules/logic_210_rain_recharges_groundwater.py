def apply(world):
    world.groundwater = (world.groundwater + world.rain * 0.02).clamp(0.0, 1.0)
