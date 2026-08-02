from datetime import datetime, UTC

from openmodellab.genome.inspectors.latency import inspect_latency
from openmodellab.genome.inspectors.memory import inspect_memory
from openmodellab.genome.inspectors.throughput import inspect_throughput
from openmodellab.genome.inspectors.batch import inspect_batch_scaling


def analyze_benchmark(model, tokenizer):
    return {
        "report": {
            "tool": "OpenModelLab",
            "tool_version": "0.1.0-alpha",
            "schema_version": "1.0",
            "generated_at": datetime.now(UTC).isoformat(),
        },
        "latency": inspect_latency(
            model,
            tokenizer
        ),
        "memory": inspect_memory(
            model,
            tokenizer
        ),
        "throughput": inspect_throughput(
            model,
            tokenizer
        ),
        "batch_scaling": inspect_batch_scaling(
            model,
            tokenizer
        )
    }
