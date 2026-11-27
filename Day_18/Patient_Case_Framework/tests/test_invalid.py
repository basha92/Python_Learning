import pytest

from validation import PatientValidator

@pytest.mark.negative
def test_invalid_patient(invalid_patient):
    with pytest.raises(ValueError):
        PatientValidator.validate(invalid_patient)

@pytest.mark.negative
def test_invalid_age(patient_with_invalid_age):
    with pytest.raises(ValueError):
        PatientValidator.validate(patient_with_invalid_age)

@pytest.mark.negative
def test_invalid_id(patient_with_invalid_id):
    with pytest.raises(ValueError):
        PatientValidator.validate(patient_with_invalid_id)

@pytest.mark.negative
def test_invalid_surgery(patient_with_invalid_surgery):
    with pytest.raises(ValueError):
        PatientValidator.validate(patient_with_invalid_surgery)