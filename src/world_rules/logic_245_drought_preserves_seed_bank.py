def apply(world):
    world.seed_bank = (world.seed_bank + (1.0 - world.soil_moisture).clamp(0.0, 1.0) * 0.002).clamp(0.0, 1.0)
