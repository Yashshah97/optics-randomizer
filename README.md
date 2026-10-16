# Optics Monte Carlo Engine

This Monte Carlo engine simulates complex optical systems by running multiple random experiments to estimate the behavior of light rays under various conditions. With built-in support for computing confidence intervals, it provides a robust and accurate tool for analyzing lens systems and other optical phenomena. Written entirely in pure Python, this project is easy to integrate into any existing workflow or research endeavor.

## What makes it unique

Combines lens systems and ray tracing with a Monte Carlo experiment runner with confidence intervals — a niche where few ready-made tools exist.

## Features

- **`optics_randomizer/montecarlo_engine.py`** — The core Monte Carlo engine functionality
- **`optics_randomizer/ray_tracer.py`** — Handles ray tracing operations for the lens system
- **`optics_randomizer/experiment_runner.py`** — Manages running Monte Carlo experiments with CI
- **`optics_randomizer/stats_calculator.py`** — Calculates statistics and confidence intervals from results
- **`optics_randomizer/utils.py`** — Miscellaneous utility functions for the project
- **`optics_randomizer/main.py`** — Entry point for running the Monte Carlo engine

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/optics-randomizer.git
cd optics-randomizer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
optics-randomizer/
├── optics_randomizer/
│   ├── montecarlo_engine.py
│   ├── ray_tracer.py
│   ├── experiment_runner.py
│   ├── stats_calculator.py
│   ├── utils.py
│   ├── main.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **optics** · Archetype: **randomizer** ·
Built autonomously by JARVIS on 2026-10-15. MIT licensed.
