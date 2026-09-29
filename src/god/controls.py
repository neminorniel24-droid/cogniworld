"""
God controls: external commands that pause, speed up, or directly intervene
in a running simulation -- kill, spawn, famine, feast, seed disease -- issued
via the server's /control/* endpoints and the dashboard buttons.

Commands are queued from the FastAPI request thread (thread-safe) and
applied once per tick inside sim_loop, which is the only place that touches
the simulation tensors. That keeps this lock-simple instead of sprinkling
locks through every tensor op in the main loop.

Population is fixed-size by design (see evolution/loop.py, reproduce()) --
spawn fills currently-dead slots immediately rather than growing the
population past config["n_agents"]. If every slot is already alive, spawn
has nothing to do.
"""
import threading

import torch

from disease.sir import SUSCEPTIBLE


def _clamp_region(region: dict, world_size: int):
    x0 = max(0, min(int(region.get("x0", 0)), world_size - 1))
    y0 = max(0, min(int(region.get("y0", 0)), world_size - 1))
    x1 = max(0, min(int(region.get("x1", world_size - 1)), world_size - 1))
    y1 = max(0, min(int(region.get("y1", world_size - 1)), world_size - 1))
    if x1 < x0:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0
    return x0, y0, x1, y1


def region_mask(agents, region, world_size: int) -> torch.Tensor:
    """Boolean mask of agents whose position falls in region. region=None
    (or omitted) means everyone."""
    if not region:
        return torch.ones(agents.n, dtype=torch.bool, device=agents.device)
    x0, y0, x1, y1 = _clamp_region(region, world_size)
    x, y = agents.pos[:, 0], agents.pos[:, 1]
    return (x >= x0) & (x <= x1) & (y >= y0) & (y <= y1)


class GodControls:
    def __init__(self):
        self._lock = threading.Lock()
        self.paused = False
        self.speed = 1.0
        self._queue = []  # list of (kind, payload dict), drained each tick

    # ---- called from HTTP handlers, any thread ----------------------
    def set_paused(self, paused: bool):
        with self._lock:
            self.paused = bool(paused)

    def set_speed(self, speed: float):
        with self._lock:
            self.speed = max(0.1, min(10.0, float(speed)))

    def queue(self, kind: str, **payload):
        with self._lock:
            self._queue.append((kind, payload))

    def snapshot(self) -> dict:
        with self._lock:
            return {"paused": self.paused, "speed": self.speed, "queued_commands": len(self._queue)}

    def _drain(self):
        with self._lock:
            items, self._queue = self._queue, []
            return items

    # ---- called once per tick from sim_loop, single-threaded there --
    def apply(self, agents, world, brain, disease, config, device) -> list:
        """Apply every queued command against the live sim state. Returns
        a short human-readable string per command actually applied, for
        logging / a dashboard event feed."""
        events = []
        for kind, payload in self._drain():
            handler = getattr(self, f"_apply_{kind}", None)
            if handler is None:
                events.append(f"god: unknown command '{kind}' ignored")
                continue
            events.append(handler(agents, world, brain, disease, config, device, payload))
        return events

    def _apply_kill(self, agents, world, brain, disease, config, device, payload):
        mask = agents.alive.clone()
        ids = payload.get("ids")
        if ids:
            id_mask = torch.zeros_like(mask)
            idx = torch.tensor([i for i in ids if 0 <= i < agents.n], dtype=torch.int64, device=device)
            if len(idx) > 0:
                id_mask[idx] = True
            mask &= id_mask
        else:
            mask &= region_mask(agents, payload.get("region"), world.size)
        n = int(mask.sum().item())
        agents.energy[mask] = 0.0
        agents.alive[mask] = False
        return f"god killed {n} agent(s)"

    def _apply_spawn(self, agents, world, brain, disease, config, device, payload):
        requested = max(0, int(payload.get("n", 0)))
        dead_idx = (~agents.alive).nonzero(as_tuple=True)[0]
        n = min(requested, len(dead_idx))
        if n > 0:
            dst = dead_idx[:n]
            alive_idx = agents.alive.nonzero(as_tuple=True)[0]
            if len(alive_idx) > 0:
                best = alive_idx[torch.argmax(agents.energy[alive_idx])]
                brain.mutate_into(best.expand(n), dst, config["mutation_std"])
            agents.pos[dst] = torch.randint(0, world.size, (n, 2), device=device)
            agents.energy[dst] = config["start_energy"]
            agents.alive[dst] = True
            agents.ticks_since_food[dst] = 0
            agents.infection[dst] = SUSCEPTIBLE
            agents.infection_timer[dst] = 0
        note = "" if n == requested else f" (only {n} dead slot(s) available -- population is fixed-size)"
        return f"god spawned {n} agent(s){note}"

    def _apply_famine(self, agents, world, brain, disease, config, device, payload):
        region = payload.get("region")
        x0, y0, x1, y1 = _clamp_region(region, world.size) if region else (0, 0, world.size - 1, world.size - 1)
        world.food[y0:y1 + 1, x0:x1 + 1] = 0.0
        return f"god caused {'a famine in ('+str(x0)+','+str(y0)+')-('+str(x1)+','+str(y1)+')' if region else 'a global famine'}"

    def _apply_feast(self, agents, world, brain, disease, config, device, payload):
        region = payload.get("region")
        x0, y0, x1, y1 = _clamp_region(region, world.size) if region else (0, 0, world.size - 1, world.size - 1)
        world.food[y0:y1 + 1, x0:x1 + 1] = 1.0  # matches World's food cap (see world/biome.py)
        return f"god blessed {'('+str(x0)+','+str(y0)+')-('+str(x1)+','+str(y1)+')' if region else 'the whole world'} with food"

    def _apply_seed_disease(self, agents, world, brain, disease, config, device, payload):
        n = disease.seed(agents, max(0, int(payload.get("n", 1))))
        return f"god seeded disease in {n} agent(s)"
