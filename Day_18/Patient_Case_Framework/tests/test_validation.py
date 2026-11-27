import pytest

from patients import Patient
from validation import PatientValidator

#expecting all the values to be valid so has to pass.
@pytest.mark.valid
def test_valid_patient():
    patient = Patient(1001, "Aaron", 38, "Knee Replacement")
    assert PatientValidator.validate(patient) is True

#expecting age to be valid so has to pass.
@pytest.mark.valid
def test_valid_age():
    patient = Patient(1002, "Kevin", 23, "Hip Implant")
    assert PatientValidator.validate(patient) is True

#expecting all the values to be invalid so has to pass.
@pytest.mark.negative
def test_invalid_age():
    patient = Patient(1006, "KK", 150, "Knee Replacement")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

@pytest.mark.negative
def test_invalid_name():
    patient = Patient(1005, "", 52, "Knee Replacement")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

@pytest.mark.negative
def test_invalid_id():
    patient = Patient("1004", "Sami", 45, "Knee Replacement")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)

@pytest.mark.negative
def test_invalid_surgery():
    patient = Patient(1001, "Aaron", 38, "")
    with pytest.raises(ValueError):
        PatientValidator.validate(patient)