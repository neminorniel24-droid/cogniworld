"""
World engine: generates a biome map (cave/mountain/river/desert/plains) from
procedural noise, and holds the resource (food) tensor that agents interact with.

Everything is stored as torch tensors on the target device so downstream modules
(brain, evolution) can read/write without CPU<->GPU transfers.
"""
import torch
from noise import pnoise2

# Biome IDs
PLAINS, RIVER, MOUNTAIN, DESERT, CAVE = 0, 1, 2, 3, 4

BIOME_NAMES = {
    PLAINS: "plains", RIVER: "river", MOUNTAIN: "mountain",
    DESERT: "desert", CAVE: "cave",
}

# Food regen rate per biome (per step, added to food tensor up to a cap)
BIOME_FOOD_REGEN = {
    PLAINS: 0.08, RIVER: 0.15, MOUNTAIN: 0.03, DESERT: 0.01, CAVE: 0.02,
}

# Shelter value (reduces exposure/temperature penalties later)
BIOME_SHELTER = {
    PLAINS: 0.0, RIVER: 0.1, MOUNTAIN: 0.2, DESERT: 0.0, CAVE: 0.8,
}


def _noise_grid(size: int, scale: float, octaves: int, seed: int) -> torch.Tensor:
    """Generate a 2D Perlin noise grid in [0, 1], as a CPU float tensor."""
    grid = torch.zeros((size, size), dtype=torch.float32)
    for y in range(size):
        for x in range(size):
            v = pnoise2(x * scale, y * scale, octaves=octaves, base=seed)
            grid[y, x] = v
    # normalize from roughly [-1, 1] to [0, 1]
    grid = (grid - grid.min()) / (grid.max() - grid.min() + 1e-8)
    return grid


class World:
    def __init__(self, config: dict, device: torch.device):
        self.size = config["world_size"]
        self.device = device

        elevation = _noise_grid(
            self.size, config["elevation_scale"], config["octaves"], config["seed"]
        )
        moisture = _noise_grid(
            self.size, config["moisture_scale"], config["octaves"], config["seed"] + 1000
        )

        self.elevation = elevation.to(device)
        self.moisture = moisture.to(device)
        self.biome = self._classify_biomes(self.elevation, self.moisture)

        # Food tensor: current available food per tile, capped at 1.0
        self.food = torch.zeros((self.size, self.size), device=device)
        self._food_cap = torch.ones_like(self.food)
        self._regen = self._biome_lookup(BIOME_FOOD_REGEN)
        self.shelter = self._biome_lookup(BIOME_SHELTER)

        # seed initial food so the world isn't empty at t=0
        self.food = self._regen.clone() * 5.0
        self.food.clamp_(0, 1.0)

    def _classify_biomes(self, elevation: torch.Tensor, moisture: torch.Tensor) -> torch.Tensor:
        biome = torch.full_like(elevation, PLAINS, dtype=torch.int64)
        biome[elevation > 0.75] = MOUNTAIN
        biome[(elevation < 0.75) & (moisture > 0.65)] = RIVER
        biome[(elevation < 0.4) & (moisture < 0.25)] = DESERT
        biome[(elevation > 0.5) & (elevation <= 0.75) & (moisture < 0.3)] = CAVE
        return biome

    def _biome_lookup(self, table: dict) -> torch.Tensor:
        lut = torch.zeros(len(table), device=self.device)
        for k, v in table.items():
            lut[k] = v
        return lut[self.biome]

    def step(self):
        """Regenerate food each tick, capped per tile."""
        self.food = torch.clamp(self.food + self._regen, min=torch.zeros_like(self._food_cap), max=self._food_cap)

    def biome_name_grid(self):
        """Return a CPU numpy-friendly grid of biome ids for rendering."""
        return self.biome.cpu().numpy()
