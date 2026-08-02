import time
import torch


def inspect_hardware(load_function, model_name):
    """
    Measures model loading and GPU information.
    """

    start = time.perf_counter()

    model, tokenizer = load_function(model_name)

    load_time = time.perf_counter() - start

    if torch.cuda.is_available():
        device = torch.device("cuda")
        model = model.to(device)

        torch.cuda.synchronize()

        props = torch.cuda.get_device_properties(0)

        memory_used = torch.cuda.memory_allocated(0) / (1024 ** 2)

        memory_reserved = torch.cuda.memory_reserved(0) / (1024 ** 2)

        gpu = {
            "device": str(device),
            "gpu_name": props.name,
            "gpu_total_memory_mb": round(props.total_memory / (1024 ** 2), 2),
            "gpu_memory_used_mb": round(memory_used, 2),
            "gpu_memory_reserved_mb": round(memory_reserved, 2),
            "cuda_version": torch.version.cuda,
            "torch_version": torch.__version__,
            "model_load_time_seconds": round(load_time, 3),
        }

    else:
        gpu = {
            "device": "cpu",
            "torch_version": torch.__version__,
            "model_load_time_seconds": round(load_time, 3),
        }

    return gpu
