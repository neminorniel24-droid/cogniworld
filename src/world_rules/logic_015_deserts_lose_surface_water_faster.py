import torch

def apply(world):
    world.surface_water *= torch.where(world.biome == 3, torch.tensor(0.995, device=world.surface_water.device), torch.tensor(1.0, device=world.surface_water.device))
