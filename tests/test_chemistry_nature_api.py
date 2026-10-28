from fastapi import FastAPI
from fastapi.testclient import TestClient
from chemistry_nature.api import router

app=FastAPI()
app.include_router(router)
client=TestClient(app)

def test_formula_endpoint():
    response=client.post("/chemistry-nature/formula",json={"formula":"H2O"})
    assert response.status_code==200
    assert response.json()["atom_counts"]=={"H":2,"O":1}

def test_formula_endpoint_rejects_unknown_element():
    response=client.post("/chemistry-nature/formula",json={"formula":"Xx2"})
    assert response.status_code==422

def test_balance_endpoint():
    response=client.post("/chemistry-nature/reaction/balance",json={"reaction":"H2 + O2 -> H2O"})
    assert response.status_code==200
    assert response.json()["balanced"]=="2 H2 + O2 -> 2 H2O"

def test_dataset_endpoint_identifies_teaching_subset():
    response=client.get("/chemistry-nature/datasets/elements")
    assert response.status_code==200
    assert response.json()["metadata"]["status"]=="curated_subset"
