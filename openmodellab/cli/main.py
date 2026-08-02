import argparse

from openmodellab.comparison.compare import generate_comparison

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.analyzer import analyze_model

from openmodellab.benchmark import analyze_benchmark

from openmodellab.reporting.json_writer import save_json
from openmodellab.reporting.benchmark_writer import save_benchmark


def main():

    parser = argparse.ArgumentParser(
        prog="openmodellab",
        description="OpenModelLab - Model Genome Generator"
    )

    subparsers = parser.add_subparsers(dest="command")


    # Genome command
    genome = subparsers.add_parser(
        "genome",
        help="Generate a model genome report"
    )

    genome.add_argument(
        "--model",
        required=True,
        help="Hugging Face model name"
    )


    # Compare command
    compare = subparsers.add_parser(
        "compare",
        help="Compare model reports"
    )

    compare.add_argument(
        "--reports",
        required=True,
        help="Directory containing genome and benchmark reports"
    )


    args = parser.parse_args()


    if args.command == "genome":

        print("=" * 60)
        print("OpenModelLab Genome")
        print("=" * 60)

        model, tokenizer = load_model(args.model)


        # Static genome analysis
        genome_report = analyze_model(
            args.model,
            model,
            tokenizer
        )

        genome_file = save_json(
            genome_report,
            args.model
        )


        # Performance benchmark
        benchmark_report = analyze_benchmark(
            model,
            tokenizer
        )

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



    elif args.command == "compare":

        print("=" * 60)
        print("OpenModelLab Model Comparison")
        print("=" * 60)

        results = generate_comparison(
            args.reports
        )

        for row in results:
            print()
            print(row)



if __name__ == "__main__":
    main()
