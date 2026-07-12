"""
Holds per-agent physical state (position, energy, alive flag) as tensors,
and computes sensor readings from the world for the brain to consume.

Sensor layout (8 values):
  0: local food level
  1: local shelter value
  2: own energy (normalized)
  3-6: food level in N/S/E/W neighbor tile
  7: bias (constant 1.0)
"""
import torch

MOVES = torch.tensor([
    [0, -1],  # N
    [0, 1],   # S
    [1, 0],   # E
    [-1, 0],  # W
], dtype=torch.int64)


class Agents:
    def __init__(self, n_agents: int, world_size: int, start_energy: float, device: torch.device):
        self.n = n_agents
        self.world_size = world_size
        self.device = device

        self.pos = torch.randint(0, world_size, (n_agents, 2), device=device)
        self.energy = torch.full((n_agents,), start_energy, device=device)
        self.alive = torch.ones(n_agents, dtype=torch.bool, device=device)

        self.moves = MOVES.to(device)

    def sense(self, world) -> torch.Tensor:
        x, y = self.pos[:, 0], self.pos[:, 1]
        food_here = world.food[y, x]
        shelter_here = world.shelter[y, x]
        energy_norm = (self.energy / 200.0).clamp(0, 1)

        neighbor_food = []
        for dx, dy in self.moves.tolist():
            nx = (x + dx).clamp(0, self.world_size - 1)
            ny = (y + dy).clamp(0, self.world_size - 1)
            neighbor_food.append(world.food[ny, nx])
        neighbor_food = torch.stack(neighbor_food, dim=1)  # [N, 4]

        bias = torch.ones(self.n, device=self.device)

        sensors = torch.cat([
            food_here.unsqueeze(1),
            shelter_here.unsqueeze(1),
            energy_norm.unsqueeze(1),
            neighbor_food,
            bias.unsqueeze(1),
        ], dim=1)
        return sensors

    def act(self, action_logits: torch.Tensor, world, move_cost: float, metabolism_cost: float, max_energy: float = 200.0):
        """Move each alive agent toward its argmax action, consume energy, eat food."""
        action = torch.argmax(action_logits, dim=1)  # [N]
        delta = self.moves[action]  # [N, 2]

        new_pos = self.pos + delta
        new_pos[:, 0] = new_pos[:, 0].clamp(0, self.world_size - 1)
        new_pos[:, 1] = new_pos[:, 1].clamp(0, self.world_size - 1)
        self.pos = torch.where(self.alive.unsqueeze(1), new_pos, self.pos)

        # eat: consume food at new tile, gain energy
        x, y = self.pos[:, 0], self.pos[:, 1]
        eaten = world.food[y, x].clone()
        world.food[y, x] -= eaten
        self.energy += eaten * 40.0  # food -> energy conversion

        # costs
        self.energy -= (move_cost + metabolism_cost)
        self.energy = self.energy.clamp(min=0, max=max_energy)

        # death
        self.alive &= self.energy > 0
