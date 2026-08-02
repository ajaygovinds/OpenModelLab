from transformers import AutoModel, AutoTokenizer
import torch


def load_model(model_name: str, device: str = "auto"):
    """
    Load a Hugging Face model and tokenizer.

    Parameters
    ----------
    model_name : str
        Hugging Face model ID.
    device : str
        "auto", "cpu", or "cuda".
    """

    print(f"Loading model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModel.from_pretrained(model_name)

    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"

    if device == "cuda":
        try:
            model = model.to("cuda")
        except Exception as e:
            print(f"Warning: Could not move model to CUDA ({e})")
            print("Falling back to CPU.")
            device = "cpu"

    if device == "cpu":
        model = model.to("cpu")

    return model, tokenizer
