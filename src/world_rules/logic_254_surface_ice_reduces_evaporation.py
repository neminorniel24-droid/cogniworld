def apply(world):
    world.evaporation = (world.evaporation - world.surface_ice * 0.01).clamp(0.0, 1.0)
