import json

from openmodellab.genome.inspectors.hardware import inspect_hardware

print(json.dumps(inspect_hardware(), indent=2))
