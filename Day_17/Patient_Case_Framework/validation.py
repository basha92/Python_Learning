#this file handles the validation part for patient details


class PatientValidator:

    @staticmethod
    def validate(patient):

        if not isinstance(patient.name, str) or not patient.name.strip():
            raise ValueError("Name cannot be empty.")

        if type(patient.age) is not int or not (1 <= patient.age <= 120):
            raise ValueError("Age must be between 1 and 120.")

        if type(patient.patient_id) is not int:
            raise ValueError("Patient ID must be an integer.")

        if not isinstance(patient.surgery_type, str) or not patient.surgery_type.strip():
            raise ValueError("Surgery type cannot be empty.")

        return True