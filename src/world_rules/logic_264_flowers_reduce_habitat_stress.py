def apply(world):
    world.habitat_stress = (world.habitat_stress - world.flowers * 0.001).clamp(0.0, 1.0)
