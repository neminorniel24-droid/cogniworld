def apply(world):
    world.snowpack = (world.snowpack + (1.0 - world.temperature).clamp(0.0, 1.0) * 0.03).clamp(0.0, 1.0)
