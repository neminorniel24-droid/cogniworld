def apply(world):
    world.seed_bank = (world.seed_bank + world.fire_risk * 0.003).clamp(0.0, 1.0)
