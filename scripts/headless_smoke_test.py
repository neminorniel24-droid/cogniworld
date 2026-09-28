"""Headless run of the full pipeline (no renderer/server) for a quick sanity
check on a machine without a GPU or display. Prints population stats.

Run from the repo root:  python3 scripts/headless_smoke_test.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import yaml
import torch

from world.biome import World
from genome.agents import Agents
from brain.batched_brain import BatchedBrain
from evolution.loop import reproduce
from migration.pressure import compute_move_cost

with open(os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")) as f:
    config = yaml.safe_load(f)

# smaller/faster than the real config, just for a quick run
config["n_agents"] = 300
config["world_size"] = 48
config["max_steps"] = 2000

device = torch.device("cpu")
torch.manual_seed(config["seed"])

world = World(config, device)
agents = Agents(config["n_agents"], config["world_size"], config["start_energy"], device)
brain = BatchedBrain(config["n_agents"], config["n_sensors"], config["brain_hidden"], config["n_actions"], device)

print(f"{'step':>6} {'alive':>6} {'avg_energy':>11} {'min_energy':>11} {'avg_ticks_since_food':>21} {'cum_deaths':>11}")
cum_deaths = 0
for step in range(config["max_steps"]):
    world.step()
    sensors = agents.sense(world)
    action_logits = brain.forward(sensors)
    move_cost = compute_move_cost(agents, config["move_cost"], config)
    agents.act(action_logits, world, move_cost, config["metabolism_cost"], config["max_energy"], config["food_energy_value"])
    cum_deaths += int((~agents.alive).sum().item())  # count BEFORE reproduce() respawns them
    reproduce(agents, brain, config, device)

    if step % 200 == 0 or step == config["max_steps"] - 1:
        alive = int(agents.alive.sum().item())
        avg_e = agents.energy[agents.alive].mean().item() if alive else float("nan")
        min_e = agents.energy[agents.alive].min().item() if alive else float("nan")
        avg_t = agents.ticks_since_food[agents.alive].float().mean().item() if alive else float("nan")
        print(f"{step:>6} {alive:>6} {avg_e:>11.2f} {min_e:>11.2f} {avg_t:>21.2f} {cum_deaths:>11}")

print("\nDone -- no crashes across", config["max_steps"], "ticks.")
