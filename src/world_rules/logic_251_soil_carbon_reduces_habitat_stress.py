def apply(world):
    world.habitat_stress = (world.habitat_stress - world.soil_carbon * 0.002).clamp(0.0, 1.0)
