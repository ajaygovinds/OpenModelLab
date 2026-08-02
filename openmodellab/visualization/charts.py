import matplotlib.pyplot as plt


def save_latency_chart(results, filename):

    models = [
        item["model"]
        for item in results
    ]

    latency = [
        item["latency_ms"]
        for item in results
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        models,
        latency
    )

    plt.xlabel(
        "Model"
    )

    plt.ylabel(
        "Latency (ms)"
    )

    plt.title(
        "Model Latency Comparison"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        filename
    )

    plt.close()



def save_throughput_chart(results, filename):

    models = [
        item["model"]
        for item in results
    ]

    throughput = [
        item["throughput"]
        for item in results
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        models,
        throughput
    )

    plt.xlabel(
        "Model"
    )

    plt.ylabel(
        "Samples / Second"
    )

    plt.title(
        "Model Throughput Comparison"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        filename
    )

    plt.close()
