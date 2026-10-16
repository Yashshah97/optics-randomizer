"""Demo for Optics Monte Carlo Engine."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import optics_randomizer

print("Optics Monte Carlo Engine", "v" + optics_randomizer.__version__)
print("modules:", [m for m in dir(optics_randomizer) if not m.startswith('_')])
