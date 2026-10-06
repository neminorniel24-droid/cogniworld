def apply(world):
    loss = (world.algae - 0.7).clamp(0.0, 0.3) * 0.01
    world.biodiversity = (world.biodiversity - loss).clamp(0.0, 1.0)
