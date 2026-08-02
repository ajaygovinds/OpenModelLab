import hashlib
import json
import transformers


def inspect_fingerprint(model):
    cfg = model.config.to_dict()

    config_json = json.dumps(cfg, sort_keys=True)

    sha = hashlib.sha256(config_json.encode()).hexdigest()

    signature = (
        f"{cfg.get('model_type', 'unknown')}-"
        f"{cfg.get('num_hidden_layers', '?')}L-"
        f"{cfg.get('hidden_size', '?')}H-"
        f"{cfg.get('num_attention_heads', '?')}A"
    )

    return {
        "architecture_signature": signature,
        "config_sha256": sha,
        "transformers_version": transformers.__version__,
    }
