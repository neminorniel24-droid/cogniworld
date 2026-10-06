def apply(world):
    world.fire_risk = (world.fire_risk - world.biodiversity * 0.002).clamp(0.0, 1.0)
