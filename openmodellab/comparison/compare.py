import json
import os


def load_reports(report_dir):

    models = {}

    for file in os.listdir(report_dir):

        path = os.path.join(
            report_dir,
            file
        )

        if file.endswith("_genome.json"):

            name = file.replace(
                "_genome.json",
                ""
            )

            models.setdefault(name, {})
            
            with open(path, "r") as f:
                models[name]["genome"] = json.load(f)


        elif file.endswith("_benchmark.json"):

            name = file.replace(
                "_benchmark.json",
                ""
            )

            models.setdefault(name, {})

            with open(path, "r") as f:
                models[name]["benchmark"] = json.load(f)

    return models



def generate_comparison(report_dir):

    reports = load_reports(report_dir)

    table = []


    for name, data in reports.items():

        genome = data.get(
            "genome",
            {}
        )

        benchmark = data.get(
            "benchmark",
            {}
        )


        table.append({

            "model": name,

            "parameters": genome.get(
                "model",
                {}
            ).get(
                "parameter_count"
            ),

            "layers": genome.get(
                "model",
                {}
            ).get(
                "num_hidden_layers"
            ),

            "hidden_size": genome.get(
                "model",
                {}
            ).get(
                "hidden_size"
            ),

            "latency_ms": benchmark.get(
                "latency",
                {}
            ).get(
                "average_ms"
            ),

            "throughput": benchmark.get(
                "throughput",
                {}
            ).get(
                "samples_per_second"
            )
        })


    return table
