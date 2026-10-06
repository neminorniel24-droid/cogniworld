def apply(world):
    world.algae = (world.algae - world.cloud * 0.003).clamp(0.0, 1.0)
