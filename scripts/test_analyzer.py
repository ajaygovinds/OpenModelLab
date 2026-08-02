import json

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.analyzer import analyze_model

MODEL = "sentence-transformers/all-MiniLM-L6-v2"

model, tokenizer = load_model(MODEL)

report = analyze_model(MODEL, model, tokenizer)

print(json.dumps(report, indent=2))
