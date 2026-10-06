def apply(world):
    world.humidity = (world.humidity + 0.003 * world.wetland).clamp(0.0, 1.0)
