
import json
from pathlib import Path

def read_patient(file_path):
    with open(file_path,"r") as file:
        content = json.load(file)
        #print(content)
    return content
file_path = Path("Day_06/data/patients.json")
patients = read_patient(file_path)
for patient in patients:
    print(patient["name"])