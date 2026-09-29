from fastapi.testclient import TestClient

import server

client = TestClient(server.app)  # not a context manager -- avoids running startup/sim thread


def reset_god():
    server.GOD.set_paused(False)
    server.GOD.set_speed(1.0)
    server.GOD._queue = []


def test_pause_endpoint_sets_flag():
    reset_god()
    r = client.post("/control/pause", json={"paused": True})
    assert r.status_code == 200 and r.json()["paused"] is True
    r = client.post("/control/pause", json={"paused": False})
    assert r.json()["paused"] is False


def test_speed_endpoint_sets_and_clamps():
    reset_god()
    assert client.post("/control/speed", json={"speed": 4}).json()["speed"] == 4.0
    assert client.post("/control/speed", json={"speed": 999}).json()["speed"] == 10.0


def test_kill_endpoint_queues_a_command():
    reset_god()
    r = client.post("/control/kill", json={"ids": [1, 2, 3]})
    assert r.json()["queued_commands"] == 1


def test_spawn_famine_feast_seed_disease_endpoints_all_queue():
    reset_god()
    client.post("/control/spawn", json={"n": 5})
    client.post("/control/famine", json={"region": {"x0": 0, "y0": 0, "x1": 5, "y1": 5}})
    client.post("/control/feast", json={})
    r = client.post("/control/seed_disease", json={"n": 3})
    assert r.json()["queued_commands"] == 4


def test_control_state_get_reflects_current_settings():
    reset_god()
    client.post("/control/pause", json={"paused": True})
    r = client.get("/control/state")
    assert r.json() == {"paused": True, "speed": 1.0, "queued_commands": 0}


def test_state_endpoint_includes_controls_and_events():
    server.STATE["controls"] = {"paused": True, "speed": 2.0, "queued_commands": 0}
    server.STATE["events"] = ["god killed 3 agent(s)"]
    r = client.get("/state")
    body = r.json()
    assert body["controls"]["paused"] is True
    assert body["events"] == ["god killed 3 agent(s)"]
