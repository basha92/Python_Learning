#this program uses JSON inputs to calcualte BMI and adds it to patient data.
import json
from pathlib import Path

def bmi_calculator(file_path):
    with open(file_path,"r") as file:
        patients = json.load(file)
        for patient in patients:
            weight = patient["weight"]
            height = patient["height"]
            patient["bmi"] = weight / (height ** 2)

    with open(file_path,"w") as file:
        json.dump(patients, file, indent=2)
    return patients
file_path = Path("Day_06/data/patients.json")
patients = bmi_calculator(file_path)
print(patients)
