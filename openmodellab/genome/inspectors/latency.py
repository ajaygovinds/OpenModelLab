import statistics
import time

import torch


def inspect_latency(
    model,
    tokenizer,
    text="OpenModelLab is benchmarking Hugging Face models.",
    warmup_runs=5,
    benchmark_runs=20,
):
    model.eval()

    # Use the device where the model already lives.
    current_device = next(model.parameters()).device
    device = str(current_device)

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
    )

    # Move only the input tensors.
    inputs = {
        key: value.to(current_device)
        for key, value in inputs.items()
    }

    # Warm-up
    with torch.no_grad():
        for _ in range(warmup_runs):
            _ = model(**inputs)

    if device.startswith("cuda"):
        torch.cuda.synchronize()

    timings = []

    # Benchmark
    with torch.no_grad():
        for _ in range(benchmark_runs):

            if device.startswith("cuda"):
                torch.cuda.synchronize()

            start = time.perf_counter()

            _ = model(**inputs)

            if device.startswith("cuda"):
                torch.cuda.synchronize()

            end = time.perf_counter()

            timings.append((end - start) * 1000)

    return {
        "device": device,
        "warmup_runs": warmup_runs,
        "benchmark_runs": benchmark_runs,
        "average_ms": round(statistics.mean(timings), 3),
        "min_ms": round(min(timings), 3),
        "max_ms": round(max(timings), 3),
        "std_ms": round(statistics.stdev(timings), 3),
    }
