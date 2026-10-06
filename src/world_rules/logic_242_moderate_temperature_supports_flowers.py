def apply(world):
    world.flowers = (world.flowers + (1.0 - (world.temperature - 0.5).abs() * 2.0).clamp(0.0, 1.0) * 0.01).clamp(0.0, 1.0)
