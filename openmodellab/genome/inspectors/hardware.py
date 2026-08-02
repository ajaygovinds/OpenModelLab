import torch


def inspect_hardware():
    report = {
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "cuda_version": torch.version.cuda,
        "device_count": torch.cuda.device_count(),
    }

    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)

        free_mem, total_mem = torch.cuda.mem_get_info()

        report.update({
            "device": "cuda:0",
            "gpu_name": props.name,
            "gpu_total_memory_mb": round(total_mem / 1024 / 1024, 2),
            "gpu_free_memory_mb": round(free_mem / 1024 / 1024, 2),
            "gpu_compute_capability": f"{props.major}.{props.minor}",
        })
    else:
        report["device"] = "cpu"

    return report
