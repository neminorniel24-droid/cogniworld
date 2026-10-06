def apply(world):
    gain = (0.3 - world.algae).clamp(0.0, 0.3) * 0.005
    world.biodiversity = (world.biodiversity + gain).clamp(0.0, 1.0)
