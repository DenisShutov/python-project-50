import json as json_module


def json(data):
    json_data = json_module.dumps(data, indent=2)
    return json_data