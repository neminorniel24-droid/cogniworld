"""
Per-agent emotion state, batched as tensors so it costs nothing extra on GPU.

Four emotions, each in [0, 1]:
  fear         - rises when energy is critically low or in a hostile biome
  hunger       - inverse of energy fraction
  curiosity    - slow random drift, resets when an agent finds food
  contentment  - rises with energy and being in a "safe" biome (shelter)

These feed back into the brain's sensors (so emotion actually influences
behavior) and drive goal selection + the procedural thought text.
"""
import torch

N_EMOTIONS = 4
FEAR, HUNGER, CURIOSITY, CONTENTMENT = 0, 1, 2, 3
EMOTION_NAMES = ["fear", "hunger", "curiosity", "contentment"]


class EmotionState:
    def __init__(self, n_agents: int, device: torch.device):
        self.device = device
        self.values = torch.zeros(n_agents, N_EMOTIONS, device=device)
        self.values[:, CURIOSITY] = torch.rand(n_agents, device=device)

    def update(self, agents, world, ate_food: torch.Tensor):
        """ate_food: bool tensor [N], True where the agent just ate this tick."""
        energy_frac = (agents.energy / 200.0).clamp(0, 1)

        self.values[:, HUNGER] = 1.0 - energy_frac
        self.values[:, CONTENTMENT] = energy_frac * 0.7 + agents.shelter_here(world) * 0.3

        # fear rises sharply as energy nears zero
        self.values[:, FEAR] = torch.clamp((0.25 - energy_frac) * 4.0, 0, 1)

        # curiosity: slow random walk, damped toward 0.5, reset low on eating (satisfied)
        drift = (torch.rand(self.values.shape[0], device=self.device) - 0.5) * 0.05
        self.values[:, CURIOSITY] = (self.values[:, CURIOSITY] + drift).clamp(0, 1)
        self.values[ate_food, CURIOSITY] *= 0.3

        self.values.clamp_(0, 1)

    def dominant(self, idx: int) -> str:
        row = self.values[idx]
        return EMOTION_NAMES[int(torch.argmax(row).item())]

    def as_list(self, idx: int):
        return self.values[idx].tolist()
