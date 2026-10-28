"""Optional FastAPI router; include it in CogniWorld's existing app factory."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .formula import molar_mass, parse_formula
from .reactions import balance_reaction
from .ecology import simulate_carbon_cycle
from .green_chemistry import e_factor
from .datasets import load_reference_dataset, load_natural_process_dataset
router=APIRouter(prefix="/chemistry-nature",tags=["chemistry-nature"])
class FormulaRequest(BaseModel):
    formula: str=Field(min_length=1,max_length=128)
class ReactionRequest(BaseModel):
    reaction: str=Field(min_length=3,max_length=512)
    max_coefficient: int=Field(default=12,ge=1,le=24)
class CarbonCycleRequest(BaseModel):
    reservoirs: dict[str,float]
    flows: list[dict]
    steps: int=Field(ge=0,le=10000)
    dt: float=Field(default=1.0,gt=0)
class EFactorRequest(BaseModel):
    waste_mass: float=Field(ge=0)
    product_mass: float=Field(gt=0)
@router.get("/health")
def health():
    return {"status":"ok","module":"chemistry-nature","scope":"calculations and illustrative models only"}
@router.post("/formula")
def formula(req: FormulaRequest):
    try: return {"formula":req.formula,"atom_counts":parse_formula(req.formula),"molar_mass_g_mol":molar_mass(req.formula)}
    except ValueError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.post("/reaction/balance")
def reaction(req: ReactionRequest):
    try: return {"input":req.reaction,"balanced":balance_reaction(req.reaction,max_coefficient=req.max_coefficient)}
    except ValueError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.post("/ecology/carbon-cycle")
def carbon_cycle(req: CarbonCycleRequest):
    try: return {"reservoirs":simulate_carbon_cycle(req.reservoirs,req.flows,steps=req.steps,dt=req.dt),"model_note":"Illustrative model, not a calibrated forecast."}
    except (ValueError,ArithmeticError) as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.post("/green-chemistry/e-factor")
def factor(req: EFactorRequest):
    try: return {"e_factor":e_factor(waste_mass=req.waste_mass,product_mass=req.product_mass),"definition":"waste mass / product mass; units must match"}
    except ValueError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.get("/datasets/elements")
def elements(): return load_reference_dataset()
@router.get("/datasets/natural-processes")
def natural_processes(): return load_natural_process_dataset()
