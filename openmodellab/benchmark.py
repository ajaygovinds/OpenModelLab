from openmodellab.genome.inspectors.latency import inspect_latency
from openmodellab.genome.inspectors.memory import inspect_memory


def analyze_benchmark(model, tokenizer):
    return {
        "latency": inspect_latency(
            model,
            tokenizer
        ),
        "memory": inspect_memory(
            model,
            tokenizer
        )
    }
