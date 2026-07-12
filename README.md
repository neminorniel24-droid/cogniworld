# CogniWorld

A GPU-accelerated artificial life simulation: agents with small evolving neural
"brains" live, forage, reproduce, and die across a procedurally generated
world of plains, rivers, mountains, deserts, and caves. No scripted behavior —
everything you see emerges from selection pressure on randomly mutated brains.

Everything runs as batched PyTorch tensors, so thousands of agents' brains
execute as a single GPU matmul per tick instead of a per-agent Python loop.

## Setup

Requires Python 3.12 (PyTorch does not yet support 3.13+/3.14) and an NVIDIA
GPU with CUDA drivers installed on the host (WSL2 users: install the driver
on the **Windows side**, not inside WSL).

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Verify GPU is visible:

```bash
python3 -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

## Run

**Pygame view (fast, local window):**
```bash
python3 src/sim.py
```

**Web dashboard (recommended — live specimen inspector, click any agent):**
```bash
cd src
uvicorn server:app --host 0.0.0.0 --port 8000
```
Then open `http://localhost:8000` in a browser. Click any dot to inspect that
agent's live emotion state, current goal, and procedurally-generated thought.

Tune population size, world size, mutation rate, etc. in `configs/default.yaml`.

## Architecture

| Module | Responsibility |
|---|---|
| `src/world/` | Biome generation (Perlin noise → elevation/moisture → biome types), food regeneration |
| `src/genome/` | Agent physical state (position, energy), sensor extraction |
| `src/brain/` | Batched MLP — every agent's brain runs as one `torch.bmm` call |
| `src/evolution/` | Fitness-weighted selection, reproduction, mutation (genetic algorithm — no backprop) |
| `src/emotion/` | Batched per-agent emotion vector (fear, hunger, curiosity, contentment) |
| `src/cognition/` | Rule-based goal selection + procedural thought-text generation (no LLM) |
| `src/memory/` | Lightweight per-agent episodic memory (ring buffer, stands in for ChromaDB/Redis until needed) |
| `src/server.py` | FastAPI backend — runs the sim continuously, serves live state as JSON |
| `web/` | Browser dashboard — biome canvas + click-to-inspect specimen panel |
| `src/disease/` | *(planned)* SIR epidemic model over agent population |
| `src/conflict/` | *(planned)* Tribe formation and combat over territory |
| `src/time_control/` | *(planned)* Pause/rewind/speed via world-state snapshots |
| `src/viz/` | Standalone pygame renderer (simpler alternative to the web dashboard) |

## Roadmap

- [x] Phase 1: biome world + batched brains + energy-driven evolution
- [ ] Phase 2: migration pressure (scarcity-driven movement between biomes)
- [ ] Phase 3: SIR disease model, density-driven outbreaks
- [ ] Phase 4: knowledge/tech accumulation + diffusion between nearby agents
- [ ] Phase 5: tribe formation + territorial conflict
- [ ] Phase 6: time control UI (pause, rewind, speed slider)

## Notes

Agent brains are direct-encoded (the weight matrices *are* the genome) and
evolved via mutation + fitness-weighted parent selection — not gradient
descent. This is intentionally simple and cheap; lifetime learning (RL or
Hebbian plasticity on top of evolved weights) is a possible future stretch
goal, not a requirement for interesting emergent behavior.
