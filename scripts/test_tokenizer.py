import json

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.inspectors.tokenizer import inspect_tokenizer

MODEL = "sentence-transformers/all-MiniLM-L6-v2"

_, tokenizer = load_model(MODEL)

report = inspect_tokenizer(tokenizer)

print(json.dumps(report, indent=2))
