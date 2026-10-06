def apply(world):
    world.seed_bank = (world.seed_bank + world.organic_matter * 0.002).clamp(0.0, 1.0)
