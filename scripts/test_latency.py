from openmodellab.genome.model_loader import load_model
from openmodellab.genome.inspectors.latency import inspect_latency

MODEL = "sentence-transformers/all-MiniLM-L6-v2"

print(f"Loading model: {MODEL}")

model, tokenizer = load_model(
        MODEL,
        device="cuda",
        )

report = inspect_latency(
    model,
    tokenizer,
)

print(report)
