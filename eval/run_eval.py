"""Reproducible evaluation entry point.

Run:  python eval/run_eval.py
Writes eval/out/results.json. Paste the headline numbers into README.md (Results)
and keep this script runnable by anyone: fixed seed, pinned data, no private inputs.
"""

import json
import pathlib
import random

SEED = 1234


def evaluate() -> dict:
    random.seed(SEED)
    # Replace with the real metric (WER, latency p50/p95, accuracy, cost per minute...).
    return {"seed": SEED, "metrics": {"example_metric": 0.0}}


if __name__ == "__main__":
    out = pathlib.Path(__file__).parent / "out"
    out.mkdir(exist_ok=True)
    (out / "results.json").write_text(json.dumps(evaluate(), indent=2))
    print("wrote", out / "results.json")
