def apply(world):
    world.deadwood = (world.deadwood - world.fire_risk * 0.02).clamp(0.0, 1.0)
