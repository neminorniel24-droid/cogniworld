def apply(world):
    world.habitat_stress = (world.habitat_stress - 0.003 * world.nutrients).clamp(0.0, 1.0)
