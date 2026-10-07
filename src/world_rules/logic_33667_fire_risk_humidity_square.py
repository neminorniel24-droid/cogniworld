import torch

def apply(world):
    src = world.fire_risk
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.humidity = torch.clamp(world.humidity + delta, -2.0, 2.0)
