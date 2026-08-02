import time
import torch


def inspect_batch_scaling(
    model,
    tokenizer,
    batch_sizes=None,
):
    if batch_sizes is None:
        batch_sizes = [1, 2, 4, 8]

    model.eval()

    device = next(model.parameters()).device

    results = []

    for batch_size in batch_sizes:

        texts = [
            "OpenModelLab batch benchmark."
            for _ in range(batch_size)
        ]

        inputs = tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128,
        )

        inputs = {
            key: value.to(device)
            for key, value in inputs.items()
        }

        with torch.no_grad():
            _ = model(**inputs)

        if str(device).startswith("cuda"):
            torch.cuda.synchronize()

        start = time.perf_counter()

        with torch.no_grad():
            _ = model(**inputs)

        if str(device).startswith("cuda"):
            torch.cuda.synchronize()

        end = time.perf_counter()

        latency_ms = (end - start) * 1000

        results.append({
            "batch_size": batch_size,
            "latency_ms": round(latency_ms, 3),
            "samples_per_second": round(
                batch_size / (end - start),
                3
            )
        })

    return {
        "device": str(device),
        "batch_sizes": batch_sizes,
        "results": results
    }
