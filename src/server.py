"""
Runs the CogniWorld simulation continuously in a background thread and
serves its live state over HTTP for the web dashboard to render.

Run with:
    uvicorn server:app --reload --host 0.0.0.0 --port 8000

Then open http://localhost:8000 in a browser.
"""
import sys
import os
import mimetypes
import threading
import time

import yaml
import torch
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

sys.path.insert(0, os.path.dirname(__file__))

from world.biome import World
from genome.agents import Agents
from brain.batched_brain import BatchedBrain
from evolution.loop import reproduce
from migration.pressure import compute_move_cost
from disease.sir import DiseaseModel
from emotion.state import EmotionState
from cognition.goals import select_goals, GOAL_NAMES
from cognition.thoughts import generate_thought
from memory.store import MemoryStore

app = FastAPI()

WEB_DIR = os.path.join(os.path.dirname(__file__), "..", "web")
mimetypes.add_type("text/javascript", ".mjs")  # browsers refuse ES modules served with another type
app.mount("/web", StaticFiles(directory=WEB_DIR), name="web")

DISEASE_NAMES = ["susceptible", "infected", "recovered"]


def terrain_payload(world) -> dict:
    """Static terrain for the 3D viewer: elevation (0..1) and biome id per tile.
    Sent once -- the world's terrain never changes during a run."""
    return {
        "size": int(world.size),
        "elevation": [[round(v, 3) for v in row] for row in world.elevation.cpu().tolist()],
        "biome": world.biome.cpu().tolist(),
    }

STATE_LOCK = threading.Lock()
STATE = {"step": 0, "alive": 0, "agents": [], "biome": None, "terrain": None,
         "disease": {"susceptible": 0, "infected": 0, "recovered": 0}}


def load_config(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "configs", "default.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def sim_loop():
    config = load_config()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[sim] using device: {device}")

    torch.manual_seed(config["seed"])

    world = World(config, device)
    agents = Agents(config["n_agents"], config["world_size"], config["start_energy"], device)
    brain = BatchedBrain(
        config["n_agents"], config["n_sensors"], config["brain_hidden"],
        config["n_actions"], device,
    )
    emotions = EmotionState(config["n_agents"], device)
    memory = MemoryStore(config["n_agents"])
    disease = DiseaseModel(config, config["world_size"], device)

    with STATE_LOCK:
        STATE["biome"] = world.biome_name_grid().tolist()
        STATE["terrain"] = terrain_payload(world)

    step = 0
    while step < config["max_steps"]:
        world.step()

        sensors = agents.sense(world)
        action_logits = brain.forward(sensors)
        move_cost = compute_move_cost(agents, config["move_cost"], config)
        ate_food = agents.act(
            action_logits, world, move_cost, config["metabolism_cost"], config["max_energy"], config["food_energy_value"]
        )

        # runs before the death snapshot below so disease deaths get logged too
        if step == config["disease_seed_step"]:
            disease.seed(agents, config["disease_initial_infected"])
        disease.step(agents)

        emotions.update(agents, world, ate_food)
        goals = select_goals(emotions.values)

        newly_dead = (~agents.alive).nonzero(as_tuple=True)[0]
        if len(newly_dead) > 0:
            memory.log_many(newly_dead.tolist(), step, "died")
        ate_idx = ate_food.nonzero(as_tuple=True)[0]
        if len(ate_idx) > 0:
            memory.log_many(ate_idx.tolist()[:50], step, "ate food")  # cap logging cost

        reproduce(agents, brain, config, device)
        for i in newly_dead.tolist():
            memory.resize_slot(i)

        # publish a lightweight snapshot every few steps (avoid locking every tick)
        if step % 2 == 0:
            alive_idx = agents.alive.nonzero(as_tuple=True)[0]
            pos = agents.pos[alive_idx].cpu().tolist()
            energy = agents.energy[alive_idx].cpu().tolist()
            goal_ids = goals[alive_idx].cpu().tolist()
            emo_vals = emotions.values[alive_idx].cpu().tolist()
            infection_ids = agents.infection[alive_idx].cpu().tolist()
            x_coord = agents.pos[alive_idx, 0].cpu().tolist()
            y_coord = agents.pos[alive_idx, 1].cpu().tolist()
            biome_grid = world.biome

            agent_records = []
            for j, real_idx in enumerate(alive_idx.tolist()):
                bx, by = int(x_coord[j]), int(y_coord[j])
                biome_id = int(biome_grid[by, bx].item())
                agent_records.append({
                    "id": real_idx,
                    "x": bx, "y": by,
                    "energy": round(energy[j], 1),
                    "goal": GOAL_NAMES[goal_ids[j]],
                    "emotion": emo_vals[j],
                    "thought": generate_thought(goal_ids[j], biome_id),
                    "infection": DISEASE_NAMES[int(infection_ids[j])],
                })

            with STATE_LOCK:
                STATE["step"] = step
                STATE["alive"] = int(agents.alive.sum().item())
                STATE["agents"] = agent_records
                STATE["disease"] = disease.counts(agents)

        step += 1
        time.sleep(0.03)  # cap sim rate so the dashboard can keep up


@app.get("/state")
def get_state():
    with STATE_LOCK:
        return {"step": STATE["step"], "alive": STATE["alive"], "agents": STATE["agents"],
                "disease": STATE["disease"]}


@app.get("/biome")
def get_biome():
    with STATE_LOCK:
        return {"biome": STATE["biome"]}


@app.get("/terrain")
def get_terrain():
    with STATE_LOCK:
        terrain = STATE["terrain"]
    if terrain is None:
        raise HTTPException(status_code=503, detail="world not ready yet")
    return terrain


@app.get("/3d")
def viewer_3d():
    return FileResponse(os.path.join(WEB_DIR, "world3d.html"))


@app.get("/")
def index():
    return FileResponse(os.path.join(os.path.dirname(__file__), "..", "web", "index.html"))


@app.on_event("startup")
def start_background_sim():
    thread = threading.Thread(target=sim_loop, daemon=True)
    thread.start()
