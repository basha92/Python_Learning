import pytest

from patients import Patient
from validation import PatientValidator

#1.testing valid ages
#@pytest.mark.parametrize("age",  [23, 45, 1, 120])
#def test_valid_age(age):
    #patient = Patient(1002, "Kevin", age, "Hip Implant")
    #assert PatientValidator.validate(patient) is True

#2.testing invalid ages
@pytest.mark.parametrize("age",  [0, -1, 121, 150])
def test_invalid_age(age):
    patient = Patient(1006, "KK", age, "Knee Replacement")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

#3. Invalid Patient IDs
@pytest.mark.parametrize("patient_id", ['1001', 10.5, ""])
def test_invalid_id(patient_id):
    patient = Patient(patient_id, "Sami", 45, "Knee Replacement")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

#4. Invalid names
@pytest.mark.parametrize("name", ["", "     "])
def test_invalid_name(name):
    patient = Patient(1005, name, 52, "Knee Replacement")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

#5. Invalid surgery type
@pytest.mark.parametrize("surgery_type", ["", "   ", None])
def test_invalid_surgery(surgery_type):
    patient = Patient(1001, "Aaron", 38, surgery_type)
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

#5.multiple valid patients
@pytest.mark.parametrize(
    "patient_id, name, age, surgery",
    [
        (1001, "Aaron", 38, "Knee Replacement"),
        (1002, "Kevin", 23, "Hip Implant"),
        (1003, "Sam", 45, "Hip Replacement")
    ]
)
def test_valid_patients(patient_id, name, age, surgery):
    patient = Patient(patient_id, name, age, surgery)
    assert PatientValidator.validate(patient) is True