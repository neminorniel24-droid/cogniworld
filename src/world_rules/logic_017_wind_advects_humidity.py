import torch

def apply(world):
    world.humidity = 0.5 * world.humidity + 0.5 * torch.roll(world.humidity, shifts=1, dims=1)
