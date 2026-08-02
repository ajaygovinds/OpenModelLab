from tabulate import tabulate


def print_table(results):

    rows = []

    for item in results:

        rows.append([
            item["model"],
            round(
                item["parameters"] / 1_000_000,
                2
            ) if item["parameters"] else None,
            item["layers"],
            item["hidden_size"],
            item["latency_ms"],
            item["throughput"]
        ])

    print()

    print(
        tabulate(
            rows,
            headers=[
                "Model",
                "Params(M)",
                "Layers",
                "Hidden",
                "Latency(ms)",
                "Throughput"
            ],
            tablefmt="grid"
        )
    )
