> A GPU-accelerated artificial life simulation where evolution, cognition, emotion, and survival emerge from simple rules.
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
For WSL2 users, install the NVIDIA driver on the Windows side so CUDA can be accessed from WSL.
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

## Testing

```bash
pip install -r requirements-dev.txt
pytest
```
Covers the pure-logic modules (brain, agents, emotion, goals, world, memory,
evolution, migration) on CPU — no GPU required. Runs automatically on every
push/PR via GitHub Actions (`.github/workflows/tests.yml`).

For an end-to-end sanity check without a GPU or display, run
`python3 scripts/headless_smoke_test.py` -- it runs the full pipeline for a
couple thousand ticks and prints population stats.

## Architecture

| Module | Responsibility |
|---|---|
| `src/world/` | Biome generation (Perlin noise → elevation/moisture → biome types), food regeneration |
| `src/genome/` | Agent physical state (position, energy), sensor extraction |
| `src/brain/` | Batched MLP — every agent's brain runs as one `torch.bmm` call |
| `src/evolution/` | Fitness-weighted selection, reproduction, mutation (genetic algorithm — no backprop) |
| `src/emotion/` | Batched per-agent emotion vector (fear, hunger, curiosity, contentment) |
| `src/cognition/` | Rule-based goal selection + procedural thought-text generation (no LLM) |
| `src/migration/` | Scarcity-driven move cost discount — cheaper movement for agents starving in place |
| `src/disease/` | SIR disease model — density-driven spread (3x3 tile exposure), energy drain, immunity after recovery |
| `src/memory/` | Lightweight per-agent episodic memory (ring buffer, stands in for ChromaDB/Redis until needed) |
| `src/server.py` | FastAPI backend — runs the sim continuously, serves live state as JSON |
| `web/` | Browser dashboard — biome canvas + click-to-inspect specimen panel |
| `src/disease/` | *(planned)* SIR epidemic model over agent population |
| `src/conflict/` | *(planned)* Tribe formation and combat over territory |
| `src/time_control/` | *(planned)* Pause/rewind/speed via world-state snapshots |
| `src/viz/` | Standalone pygame renderer (simpler alternative to the web dashboard) |

## Roadmap

- [x] Phase 1: biome world + batched brains + energy-driven evolution
- [x] Phase 2: migration pressure (scarcity-driven movement between biomes)
- [x] Phase 3: SIR disease model, density-driven outbreaks
- [ ] Phase 4: knowledge/tech accumulation + diffusion between nearby agents
- [ ] Phase 5: tribe formation + territorial conflict
- [ ] Phase 6: time control UI (pause, rewind, speed slider)

## Disease

Agents are Susceptible, Infected or Recovered (immune). At `disease_seed_step`
an outbreak is seeded; each tick a susceptible agent catches it with
probability `1 - (1 - disease_beta) ** n`, where `n` is the number of infected
agents within its 3x3 tile neighborhood, so crowded areas spread it faster.
Infected agents lose `disease_energy_drain` extra energy per tick and can die
of it; survivors recover after `disease_duration` ticks. Newborns are always
born susceptible, which keeps supplying fresh hosts. Rule of thumb from a
sweep on the default density: `disease_beta` below ~0.06 gives one wave that
burns out, ~0.1 and above stays endemic. `/state` reports S/I/R counts and
each agent's `infection` state.

## Notes

Agent brains are direct-encoded (the weight matrices *are* the genome) and
evolved via fitness-weighted parent selection — not gradient descent.
Reproduction is sexual by default: two eligible parents (energy above
`reproduce_threshold`) each contribute roughly half their brain's weights
via uniform crossover, then Gaussian mutation is applied on top, and both
parents pay half of `reproduce_cost` in energy. Early on, or after a
population crash, there often aren't two eligible parents available yet —
in that case reproduction falls back to the original asexual path (single
parent cloned with mutation, no energy cost) so the population can recover.
Lifetime learning (RL or Hebbian plasticity on top of evolved weights) is a
possible future stretch goal, not a requirement for interesting emergent
behavior.

The default economy (`configs/default.yaml`, regen rates in `world/biome.py`)
is tuned so real death/rebirth turnover happens. At the original numbers the
whole map sat near the food cap and no agent ever ran out of energy. The
population *count* is constant either way (`reproduce()` refills a dead slot
the same tick), so check the smoke test's cumulative death counter, not the
alive count, to see whether selection pressure is doing anything.
