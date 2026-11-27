#Lesson 1: Fixture Dependencies (Building Blocks)

#The Idea: Sometimes, you need to build one LEGO piece before you can attach another piece on top of it. In pytest, one fixture can ask for another fixture to do its job first!

#Exercise 1: Fixture dependency

#1. valid_patient creates a basic patient dictionary.
#2. validated_patient takes valid_patient as an input, adds "is_valid": True to it, and hands it to the test.

import pytest

from patients import Patient
from validation import PatientValidator

# Block 1: The basic patient
@pytest.fixture
def valid_patient():
    return Patient(1001, "Aaron", 38, "Knee Replacement")  #since we are passing tuple, we can access elements as objects.
    #return {"patient_id":1001, "name":"Aaron", "age": 38, "surgery_type": "Knee Replacement"}

# Block 2: Uses Block 1 to build something bigger
# to access objects from validator. If the validator program expects a dictionary then we can pass dictionary here in the patient.
@pytest.fixture
def validated_patient(valid_patient):
    PatientValidator.validate(valid_patient)
    return valid_patient


# The Test: Asks for Block 2 (which automatically runs Block 1 first!)
def test_patient_details(validated_patient):
    assert validated_patient.patient_id == 1001
    assert validated_patient.name == "Aaron"
    assert validated_patient.age == 38
    assert validated_patient.surgery_type == "Knee Replacement"

    #assert validated_patient["patient_id"] == 1001
    #assert validated_patient["name"] == "Aaron"
    #assert validated_patient["age"] == 38
    #assert validated_patient["surgery_type"] == "Knee Replacement"
    #assert validated_patient["is_valid"] is True

