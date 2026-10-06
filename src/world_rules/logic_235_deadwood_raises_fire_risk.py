def apply(world):
    world.fire_risk = (world.fire_risk + world.deadwood * 0.003).clamp(0.0, 1.0)
