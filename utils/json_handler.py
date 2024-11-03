import json

path = './data.json'

def json_dump(task):
    with open(path, "w") as file:
        json.dump(task, file, indent=2)


def json_load():
    with open(path, "r") as file:
        return json.load(file)