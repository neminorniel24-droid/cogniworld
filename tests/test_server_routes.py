from fastapi.testclient import TestClient

import server

# Not used as a context manager on purpose: that would run the startup
# event and launch the whole simulation thread.
client = TestClient(server.app)


def test_terrain_returns_503_until_world_is_built():
    server.STATE["terrain"] = None
    assert client.get("/terrain").status_code == 503


def test_terrain_returns_payload_once_ready():
    server.STATE["terrain"] = {"size": 2, "elevation": [[0, 0], [0, 0]], "biome": [[0, 0], [0, 0]]}
    r = client.get("/terrain")
    assert r.status_code == 200 and r.json()["size"] == 2
    server.STATE["terrain"] = None


def test_3d_page_is_served():
    assert client.get("/3d").status_code == 200


def test_es_module_is_served_with_a_javascript_mime_type():
    r = client.get("/web/world3d_core.mjs")
    assert r.status_code == 200
    assert "javascript" in r.headers["content-type"]
