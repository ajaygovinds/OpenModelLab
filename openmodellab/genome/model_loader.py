from transformers import AutoModel, AutoTokenizer
import torch


def load_model(model_name: str, device: str = "auto"):

    print(f"Loading model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"

    if device == "cuda":

        try:
            model = AutoModel.from_pretrained(
                model_name
            )

            model = model.cuda()

            print(
                "Model loaded on CUDA:",
                torch.cuda.get_device_name(0)
            )

        except Exception as e:

            print("Standard CUDA loading failed.")
            print(e)

            print("Trying automatic device mapping...")

            model = AutoModel.from_pretrained(
                model_name,
                device_map="auto"
            )

    else:
        model = AutoModel.from_pretrained(
            model_name
        )

        model = model.cpu()

        print("Model loaded on CPU.")

    return model, tokenizer
