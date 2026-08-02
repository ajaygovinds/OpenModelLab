import os
import psutil
import torch


def get_process_memory_mb():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)


def inspect_memory(model, tokenizer):

    model.eval()

    device = str(next(model.parameters()).device)

    memory = {
        "device": device,
        "ram_before_mb": round(get_process_memory_mb(), 2),
    }

    text = "OpenModelLab memory benchmark."

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
    )

    inputs = {
        key: value.to(next(model.parameters()).device)
        for key, value in inputs.items()
    }

    if device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
        torch.cuda.empty_cache()

    with torch.no_grad():
        _ = model(**inputs)

    memory["ram_after_mb"] = round(get_process_memory_mb(), 2)

    if device.startswith("cuda"):
        memory["gpu_allocated_mb"] = round(
            torch.cuda.memory_allocated() / (1024 ** 2),
            2
        )

        memory["gpu_peak_allocated_mb"] = round(
            torch.cuda.max_memory_allocated() / (1024 ** 2),
            2
        )

    return memory
