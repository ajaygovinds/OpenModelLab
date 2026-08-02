import json
from pathlib import Path


def save_json(report: dict, model_name: str):
    model_dir = model_name.replace("/", "_")

    out_dir = Path("outputs") / model_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    output_file = out_dir / "genome.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return output_file
