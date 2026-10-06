def apply(world):
    world.vegetation = (world.vegetation + 0.004 * (1.0 - 2.0 * (world.temperature - 0.5).abs()).clamp(0.0, 1.0)).clamp(0.0, 1.0)
