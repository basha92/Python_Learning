from person import Person

class Patient(Person):
    def __init__(self, patient_id, name, age):
        super().__init__(name, age)
        self.patient_id = patient_id

    def display_details(self):
        print(f"PatientID: {self.patient_id}")
        super().display_details()