from huggingface_hub import model_info

from openmodellab.genome.inspectors.tokenizer import inspect_tokenizer

from openmodellab.genome.inspectors.hardware import inspect_hardware

from openmodellab.genome.inspectors.fingerprint import inspect_fingerprint

from datetime import datetime, UTC


def count_parameters(model):
    return sum(p.numel() for p in model.parameters())


def inspect_model(model_name, model):
    cfg = model.config
    info = model_info(model_name)

    return {
        "model_name": model_name,
        "architecture": model.__class__.__name__,
        "model_type": getattr(cfg, "model_type", None),
        "hidden_size": getattr(cfg, "hidden_size", None),
        "num_hidden_layers": getattr(cfg, "num_hidden_layers", None),
        "num_attention_heads": getattr(cfg, "num_attention_heads", None),
        "intermediate_size": getattr(cfg, "intermediate_size", None),
        "max_position_embeddings": getattr(cfg, "max_position_embeddings", None),
        "parameter_count": count_parameters(model),
        "dtype": str(next(model.parameters()).dtype),
        "framework": "transformers",
        "license": info.card_data.get("license") if info.card_data else None,
    }


def analyze_model(model_name, model, tokenizer):
    return {
         "report": {
            "tool": "OpenModelLab",
            "tool_version": "0.1.0-alpha",
            "schema_version": "1.0",
            "generated_at": datetime.now(UTC).isoformat(),
        },   
        "model": inspect_model(model_name, model),
        "tokenizer": inspect_tokenizer(tokenizer),
        "hardware": inspect_hardware(),
        "fingerprint": inspect_fingerprint(model),
    }
