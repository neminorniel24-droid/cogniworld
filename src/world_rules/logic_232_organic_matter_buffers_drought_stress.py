def apply(world):
    world.habitat_stress = (world.habitat_stress - world.organic_matter * 0.003).clamp(0.0, 1.0)
