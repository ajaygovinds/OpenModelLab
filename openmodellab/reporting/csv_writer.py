import csv


def save_csv(results, filename):

    with open(
        filename,
        "w",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "Model",
            "Parameters",
            "Layers",
            "Hidden Size",
            "Latency(ms)",
            "Throughput"
        ])

        for item in results:

            writer.writerow([
                item["model"],
                item["parameters"],
                item["layers"],
                item["hidden_size"],
                item["latency_ms"],
                item["throughput"]
            ])

    return filename
