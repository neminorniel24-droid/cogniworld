def apply(world):
    world.habitat_stress = (world.habitat_stress - 0.006 * world.vegetation).clamp(0.0, 1.0)
