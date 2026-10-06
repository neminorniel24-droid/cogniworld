def apply(world):
    world.sediment = (world.sediment - world.vegetation * 0.01).clamp(0.0, 1.0)
