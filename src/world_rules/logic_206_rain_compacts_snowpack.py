def apply(world):
    loss = world.rain * 0.02
    world.snowpack = (world.snowpack - loss).clamp(0.0, 1.0)
