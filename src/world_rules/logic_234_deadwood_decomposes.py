def apply(world):
    world.deadwood = (world.deadwood - world.decomposition_rate * 0.01).clamp(0.0, 1.0)
