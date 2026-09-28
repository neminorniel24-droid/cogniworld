"""
Every agent's brain is a tiny 2-layer MLP: sensors -> hidden -> actions.
Instead of looping over agents in Python, we stack every agent's weight
matrices into single tensors and run one batched matmul (torch.bmm) per tick.

Weight shapes (N = number of agents):
  W1: [N, n_sensors, hidden]
  b1: [N, hidden]
  W2: [N, hidden, n_actions]
  b2: [N, n_actions]
"""
import torch


class BatchedBrain:
    def __init__(self, n_agents: int, n_sensors: int, hidden: int, n_actions: int, device: torch.device):
        self.n_sensors = n_sensors
        self.hidden = hidden
        self.n_actions = n_actions
        self.device = device

        scale = 1.0 / (n_sensors ** 0.5)
        self.W1 = (torch.randn(n_agents, n_sensors, hidden, device=device)) * scale
        self.b1 = torch.zeros(n_agents, hidden, device=device)
        self.W2 = (torch.randn(n_agents, hidden, n_actions, device=device)) * (1.0 / hidden ** 0.5)
        self.b2 = torch.zeros(n_agents, n_actions, device=device)

    def forward(self, sensors: torch.Tensor) -> torch.Tensor:
        """
        sensors: [N, n_sensors] -> returns action logits [N, n_actions]
        """
        # [N, 1, S] @ [N, S, H] -> [N, 1, H] -> [N, H]
        h = torch.bmm(sensors.unsqueeze(1), self.W1).squeeze(1) + self.b1
        h = torch.tanh(h)
        out = torch.bmm(h.unsqueeze(1), self.W2).squeeze(1) + self.b2
        return out

    def get_genome(self, idx: torch.Tensor):
        """Extract flattened weights for the given agent indices (for reproduction)."""
        return (self.W1[idx].clone(), self.b1[idx].clone(),
                self.W2[idx].clone(), self.b2[idx].clone())

    def set_genome(self, idx: torch.Tensor, genome):
        W1, b1, W2, b2 = genome
        self.W1[idx] = W1
        self.b1[idx] = b1
        self.W2[idx] = W2
        self.b2[idx] = b2

    def mutate_into(self, src_idx: torch.Tensor, dst_idx: torch.Tensor, std: float):
        """Copy src agent's brain into dst slot with Gaussian mutation noise.

        Kept as the asexual fallback path -- used when the evolution loop
        can't find two eligible parents (see evolution/loop.py)."""
        self.W1[dst_idx] = self.W1[src_idx] + torch.randn_like(self.W1[src_idx]) * std
        self.b1[dst_idx] = self.b1[src_idx] + torch.randn_like(self.b1[src_idx]) * std
        self.W2[dst_idx] = self.W2[src_idx] + torch.randn_like(self.W2[src_idx]) * std
        self.b2[dst_idx] = self.b2[src_idx] + torch.randn_like(self.b2[src_idx]) * std

    def crossover_into(self, parent_a_idx: torch.Tensor, parent_b_idx: torch.Tensor,
                        dst_idx: torch.Tensor, std: float):
        """Sexual reproduction: for each dst slot, build a child brain by
        picking each weight independently from parent A or parent B
        (uniform crossover, ~50/50 per element), then apply Gaussian
        mutation noise on top -- same noise scale as the asexual path.
        """
        for name in ("W1", "b1", "W2", "b2"):
            tensor = getattr(self, name)
            a = tensor[parent_a_idx]
            b = tensor[parent_b_idx]
            mask = torch.rand_like(a) < 0.5
            child = torch.where(mask, a, b)
            child = child + torch.randn_like(child) * std
            tensor[dst_idx] = child
