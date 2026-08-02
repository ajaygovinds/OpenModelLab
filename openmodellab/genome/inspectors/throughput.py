import time
import torch


def inspect_throughput(
    model,
    tokenizer,
    text="OpenModelLab throughput benchmark.",
    runs=50,
):
    model.eval()

    device = next(model.parameters()).device
    device_name = str(device)

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    # Warmup
    with torch.no_grad():
        for _ in range(5):
            _ = model(**inputs)

    if device_name.startswith("cuda"):
        torch.cuda.synchronize()

    start = time.perf_counter()

    with torch.no_grad():
        for _ in range(runs):
            _ = model(**inputs)

    if device_name.startswith("cuda"):
        torch.cuda.synchronize()

    end = time.perf_counter()

    total_time = end - start

    return {
        "device": device_name,
        "runs": runs,
        "total_time_sec": round(total_time, 4),
        "samples_per_second": round(
            runs / total_time,
            3
        ),
    }
