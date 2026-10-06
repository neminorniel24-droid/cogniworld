def apply(world):
    world.habitat_stress = (world.habitat_stress - 0.002 * world.biodiversity).clamp(0.0, 1.0)
