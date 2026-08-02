import json

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.inspectors.hardware import inspect_hardware

MODEL = "sentence-transformers/all-MiniLM-L6-v2"

report = inspect_hardware(
    load_model,
    MODEL
)

print(json.dumps(report, indent=2))
