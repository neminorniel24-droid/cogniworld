"""Makes `src/` importable as top-level packages (world, genome, brain, ...)
in tests, matching how sim.py and server.py already do it via sys.path."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
