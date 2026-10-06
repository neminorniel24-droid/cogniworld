def apply(world):
    world.sediment = (world.sediment - world.root_density * 0.003).clamp(0.0, 1.0)
