def apply(world):
    world.humidity = (world.humidity + world.algae * 0.004).clamp(0.0, 1.0)
