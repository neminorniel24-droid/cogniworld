"""
Phase 1 entry point: biome world + batched evolving agents, rendered live.

Run with:
    python3 src/sim.py
"""
import sys
import os
import yaml
import torch

sys.path.insert(0, os.path.dirname(__file__))

from world.biome import World
from genome.agents import Agents
from brain.batched_brain import BatchedBrain
from evolution.loop import reproduce
from viz.renderer import Renderer


def load_config(path="configs/default.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    config = load_config()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    torch.manual_seed(config["seed"])

    world = World(config, device)
    agents = Agents(config["n_agents"], config["world_size"], config["start_energy"], device)
    brain = BatchedBrain(
        config["n_agents"], config["n_sensors"], config["brain_hidden"],
        config["n_actions"], device,
    )
    renderer = Renderer(config["world_size"])

    running = True
    step = 0
    while running and step < config["max_steps"]:
        world.step()

        sensors = agents.sense(world)
        action_logits = brain.forward(sensors)
        agents.act(action_logits, world, config["move_cost"], config["metabolism_cost"], config["max_energy"])

        reproduce(agents, brain, config, device)

        alive_count = int(agents.alive.sum().item())
        running = renderer.draw(world, agents, step, alive_count)
        step += 1

    renderer.close()


if __name__ == "__main__":
    main()
