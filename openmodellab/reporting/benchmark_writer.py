from pathlib import Path
import json


def save_benchmark(report: dict, model_name: str):
    """
    Save benchmark report as benchmark.json.
    """

    outdir = Path("outputs") / model_name.replace("/", "_")
    outdir.mkdir(parents=True, exist_ok=True)

    outfile = outdir / "benchmark.json"

    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return str(outfile)
