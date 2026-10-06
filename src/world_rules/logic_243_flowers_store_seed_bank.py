def apply(world):
    world.seed_bank = (world.seed_bank + world.flowers * 0.008).clamp(0.0, 1.0)
