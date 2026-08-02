import argparse

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.analyzer import analyze_model

from openmodellab.reporting.json_writer import save_json
from openmodellab.reporting.benchmark_writer import save_benchmark


parser = argparse.ArgumentParser()

parser.add_argument(
    "--model",
    required=True,
    help="Hugging Face model name"
)

args = parser.parse_args()

print("=" * 60)
print("OpenModelLab Genome")
print("=" * 60)

model, tokenizer = load_model(args.model)

report = analyze_model(
    args.model,
    model,
    tokenizer
)

# Save static genome information
genome_file = save_json(
    report,
    args.model
)

# Placeholder benchmark report (v0.2)
benchmark_report = {
    "status": "Benchmarking module under development"
}

benchmark_file = save_benchmark(
    benchmark_report,
    args.model
)

print()
print("Genome report saved:")
print(genome_file)

print()
print("Benchmark report saved:")
print(benchmark_file)
