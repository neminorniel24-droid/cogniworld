def apply(world):
    world.deadwood = (world.deadwood + (world.biomass - world.vegetation).clamp(0.0, 1.0) * 0.02).clamp(0.0, 1.0)
