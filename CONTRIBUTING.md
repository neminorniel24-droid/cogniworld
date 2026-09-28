# Contributing to CogniWorld

## Setup
Follow the Setup section in the README, then install dev dependencies:
```bash
pip install -r requirements-dev.txt
```

## Running tests
```bash
pytest
```
Most tests run on CPU and don't require a GPU. A few (anything touching
`BatchedBrain` or `Agents.sense`/`act`) will run on CPU fine too — CUDA is
only used automatically if `torch.cuda.is_available()`, tests don't force it.

## Code style
- Keep modules small and single-purpose (see the Architecture table in the
  README) — `world/`, `genome/`, `brain/`, `evolution/`, `emotion/`,
  `cognition/`, `memory/` each own one concern.
- Batch everything as tensors. A per-agent Python `for` loop in a hot path
  (anything called every tick) defeats the point of this project — if you
  find yourself writing one, look for the tensor-op equivalent first.
- Docstrings on every module explaining *why*, not just what — this project
  leans on them heavily since there's no LLM narrating behavior at runtime.

## Commit style
Small, atomic commits. One logical change per commit, with a message that
explains what changed and why (not just "update file"). Doesn't need to be
fancy — a one-line summary is fine for small changes, a short body is
welcome when the "why" isn't obvious from the diff alone.
