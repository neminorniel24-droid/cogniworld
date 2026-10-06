def apply(world):
    stress = (world.temperature - 0.5).abs() * 0.002
    world.pollinators = (world.pollinators - stress).clamp(0.0, 1.0)
