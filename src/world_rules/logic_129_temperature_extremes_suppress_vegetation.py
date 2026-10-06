def apply(world):
    world.vegetation = (world.vegetation * (1.0 - 0.012 * (2.0 * (world.temperature - 0.5).abs()).clamp(0.0, 1.0))).clamp(0.0, 1.0)
