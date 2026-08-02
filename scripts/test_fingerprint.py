import json

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.inspectors.fingerprint import inspect_fingerprint

MODEL = "sentence-transformers/all-MiniLM-L6-v2"

model, tokenizer = load_model(MODEL)

report = inspect_fingerprint(model)

print(json.dumps(report, indent=2))
