import torch


def inspect_precision(model):

    dtype = str(
        next(model.parameters()).dtype
    )

    mapping = {
        "torch.float32": {
            "bits": 32,
            "category": "FP32"
        },
        "torch.float16": {
            "bits": 16,
            "category": "FP16"
        },
        "torch.bfloat16": {
            "bits": 16,
            "category": "BF16"
        },
        "torch.int8": {
            "bits": 8,
            "category": "INT8"
        }
    }

    info = mapping.get(
        dtype,
        {
            "bits": None,
            "category": "unknown"
        }
    )

    return {
        "dtype": dtype,
        **info
    }
