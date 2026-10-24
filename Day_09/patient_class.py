#this example puts all patient functions created earlier inside a class.
import json
from pathlib import Path

class patient_details():
    def __init__(self, file_path):  #filepath is chosen because that's where all data is stored and it is common.
        self.file_path = Path(file_path)

    def bmi_calculator (self):
        with open(self.file_path,"r") as file:
            patients = json.load(file)
            for patient in patients:
                weight = patient["weight"]
                height = patient["height"]
                patient["bmi"] = weight / (height ** 2)

        with open(self.file_path,"w") as file:
            json.dump(patients, file, indent=2)
        return patients

#defining file path
file_path = Path("Day_06/data/patients.json")
#calling the class to store the path
patient_data = patient_details(file_path)
#calling the function to use
patients = patient_data.bmi_calculator()

print(patients)

#Notes:
#__init__() is used to initialize the object's data when you create an object. 
# In your example, you can use it to store the file_path so that your methods can access it without receiving the path every time.
#With __init__() storing the path	     |      Without storing the path
#_____________________________________________________________________
#Pass the path when creating the object	 |  Pass the path when calling the method
#patient_data.bmi_calculator()	         |   patient_data.bmi_calculator(file_path)
#Object remembers its file	             |   Each call supplies the file#

    