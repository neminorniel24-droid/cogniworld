def apply(world):
    germinate = world.seed_bank * world.soil_moisture * 0.02
    world.seed_bank = (world.seed_bank - germinate).clamp(0.0, 1.0)
    world.vegetation = (world.vegetation + germinate).clamp(0.0, 1.0)
