import torch


def inspect_execution(model, requested_device="auto"):

    actual_device = str(
        next(model.parameters()).device
    )

    cuda_available = torch.cuda.is_available()

    fallback = (
        requested_device == "cuda"
        and not actual_device.startswith("cuda")
    )

    gpu_name = None

    if cuda_available:
        gpu_name = torch.cuda.get_device_name(0)

    return {
        "requested_device": requested_device,
        "actual_device": actual_device,
        "cuda_available": cuda_available,
        "gpu_name": gpu_name,
        "fallback": fallback
    }
