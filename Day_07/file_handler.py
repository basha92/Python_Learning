import json
from pathlib import Path

def find_json_files(folder_path):
    folder = Path(folder_path)
    json_files = []
    for item in folder.iterdir():
        if item.suffix == ".json":
            json_files.append(item)
    return json_files

def read_json(folder_path):
    with open (folder_path, "r") as file:
        content = json.load(file)
    return content

def write_json(folder_path, data):
    with open (folder_path, "w") as file:
        json.dump(data, file, indent=4)
