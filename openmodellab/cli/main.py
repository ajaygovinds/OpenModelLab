import argparse

from openmodellab.genome.model_loader import load_model
from openmodellab.genome.analyzer import analyze_model
from openmodellab.reporting.json_writer import save_json


def main():

    parser = argparse.ArgumentParser(
        prog="openmodellab",
        description="OpenModelLab - Model Genome Generator"
    )

    subparsers = parser.add_subparsers(dest="command")

    genome = subparsers.add_parser(
        "genome",
        help="Generate a model genome report"
    )

    genome.add_argument(
        "--model",
        required=True,
        help="Hugging Face model name"
    )

    args = parser.parse_args()

    if args.command == "genome":

        print("=" * 60)
        print("OpenModelLab Genome")
        print("=" * 60)

        model, tokenizer = load_model(args.model)

        report = analyze_model(
            args.model,
            model,
            tokenizer
        )

        outfile = save_json(
            report,
            args.model
        )

        print()
        print("Genome report saved:")
        print(outfile)


if __name__ == "__main__":
    main()
