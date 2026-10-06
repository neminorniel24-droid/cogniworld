def apply(world):
    world.biodiversity = (world.biodiversity + world.seed_bank * 0.003).clamp(0.0, 1.0)
