def apply(world):
    world.nutrients = (world.nutrients + (world.elevation < 0.3).float() * world.sediment * 0.01).clamp(0.0, 1.0)
