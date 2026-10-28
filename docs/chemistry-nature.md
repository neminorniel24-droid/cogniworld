# CogniWorld Chemistry + Nature subsystem

## Scope
This additive package supplies a formula parser/molar-mass calculator, bounded reaction balancer, transparent ecological reservoir model, atom-economy and E-factor calculations, source-labelled element data, an explicitly illustrative natural-process dataset, and an optional FastAPI router. It is not a quantum-chemistry engine, toxicity database, lifecycle assessment, or climate forecast.

## Test-first workflow
From the repository root, after activating the project virtual environment, extract this archive while preserving paths, then run:

```bash
PYTHONPATH=src pytest -q tests/test_chemistry_nature.py tests/test_chemistry_nature_api.py
PYTHONPATH=src python scripts/smoke_chemistry_nature.py
python -m compileall -q src/chemistry_nature
git diff --check
pytest -q
```

Do not proceed to commit unless the focused and full regression suites pass. The focused tests are included in `tests/test_chemistry_nature.py`.

## Optional FastAPI integration
The repository's current server entry point is `src/server.py` and creates the shared `app = FastAPI()` instance. The archive includes `integration/server_router_snippet.py.txt`; make these two small edits to register the router on that existing app:

```python
from chemistry_nature.api import router as chemistry_nature_router
app.include_router(chemistry_nature_router)
```

Use the existing app instance, do not create a second application. Ensure `src` is on `PYTHONPATH` in the same way as the current project tests.

Endpoints:
- `GET /chemistry-nature/health`
- `POST /chemistry-nature/formula` — `{"formula":"Ca(OH)2"}`
- `POST /chemistry-nature/reaction/balance` — `{"reaction":"H2 + O2 -> H2O"}`
- `POST /chemistry-nature/ecology/carbon-cycle`
- `POST /chemistry-nature/green-chemistry/e-factor`
- `GET /chemistry-nature/datasets/elements`
- `GET /chemistry-nature/datasets/natural-processes`

## Scientific limitations and provenance
- The atomic-weight JSON is a curated teaching subset from CIAAW/IUPAC, not a full periodic table. Values are approximate. Some standard atomic weights vary by natural sample; argon is intentionally represented by a single conventional value in this starter subset.
- The ecological rates are synthetic teaching parameters. The simulator conserves total amount in a closed network and rejects an unstable explicit step; it does not predict real carbon fluxes.
- Reaction balancing uses bounded integer search, supports at most six terms and five elements, and is not suitable for arbitrary reactions.
- Atom economy supports only reactions where the listed desired product is the only product. It excludes yield, solvent, energy, and hazards.
- E-factor depends on the defined waste boundary, including whether water is counted. Document the boundary when comparing processes.

Data sources:
- CIAAW Standard Atomic Weights: https://ciaaw.org/atomic-weights.htm
- IUPAC Periodic Table: https://iupac.org/what-we-do/periodic-table/
- U.S. EPA, Basics of Green Chemistry: https://www.epa.gov/greenchemistry/basics-green-chemistry

## Follow-up work
1. Replace bounded brute-force balancing with exact rational null-space solving.
2. Add support for hydrate/charge/isotope notation with a documented grammar.
3. Add externally sourced environmental datasets with units, uncertainty, provenance, and expert review before using measured rates.
4. Add PMI, reaction mass efficiency, energy intensity, and lifecycle boundaries.
5. Add API integration tests against CogniWorld's actual app factory before enabling the router.
