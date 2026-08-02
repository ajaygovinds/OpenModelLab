from openmodellab.genome.inspectors.latency import inspect_latency


def analyze_benchmark(model, tokenizer):
    return {
        "latency": inspect_latency(
            model,
            tokenizer
        )
    }
