from openmodellab.reporting.benchmark_writer import save_benchmark

report = {
    "latency": {
        "device": "cpu",
        "average_ms": 12.34,
        "min_ms": 11.98,
        "max_ms": 13.01,
    }
}

outfile = save_benchmark(
    report,
    "sentence-transformers/all-MiniLM-L6-v2",
)

print(outfile)
