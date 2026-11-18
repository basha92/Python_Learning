#Exercise 3: Multilevel inheritance
#Create:
#Person → Patient → SurgicalPatient
#Add a patient ID in Patient and surgery type in SurgicalPatient.
#Create two surgical patient objects and display their details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Patient(Person):
    def __init__(self, patient_id, name, age):
        super().__init__(name, age)
        self.patient_id = patient_id

    def display_details(self):
        print("\nPatient Details")
        print(f"PatientID: {self.patient_id}")
        super().display_details()

class SurgicalPatient(Patient):
    def __init__(self, patient_id, name, age, surgery_type):
        super().__init__(patient_id, name, age)
        self.surgery_type = surgery_type

    def display_details(self):
        print("\nSurgery Patient Details")
        super().display_details()
        print(f"Surgery Type: {self.surgery_type}")

patient1 = SurgicalPatient("Arun","P1001",52,"Knee Replacement")
patient2 = SurgicalPatient("Kumar","P1002",40,"Hip Implant")

patient1.display_details() #no need to use print as the method uses print instead of return.
patient2.display_details()

print(SurgicalPatient.__mro__)
#(<class '__main__.SurgicalPatient'>, <class '__main__.Patient'>, <class '__main__.Person'>, <class 'object'>)