import json


def json_reader(path):
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data
