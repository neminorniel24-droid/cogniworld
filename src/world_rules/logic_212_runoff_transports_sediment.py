def apply(world):
    world.sediment = (world.sediment + world.runoff * 0.03).clamp(0.0, 1.0)
