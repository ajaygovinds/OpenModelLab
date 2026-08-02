from transformers import AutoModel, AutoTokenizer


def load_model(model_name: str):
    """
    Load a Hugging Face model and tokenizer.
    """
    print(f"Loading model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModel.from_pretrained(model_name)

    return model, tokenizer
