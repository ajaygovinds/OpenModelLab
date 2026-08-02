from openmodellab.genome.model_loader import load_model

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model, tokenizer = load_model(MODEL_NAME)

print("\nSuccess!\n")

print(type(model))
print(type(tokenizer))
