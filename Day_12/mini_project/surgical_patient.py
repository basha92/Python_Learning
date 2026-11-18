from patient import Patient

class SurgicalPatient(Patient):
    def __init__(self, patient_id, name, age, surgery_type):
        super().__init__(patient_id, name, age)
        self.surgery_type = surgery_type

    def display_details(self):
        print("\nSurgery Patient Details")
        super().display_details()
        print(f"Surgery Type: {self.surgery_type}")