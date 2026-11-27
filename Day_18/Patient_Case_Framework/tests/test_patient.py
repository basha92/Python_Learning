import pytest

from validation import PatientValidator

#fixing the input - moved this to conf test
#@pytest.fixture(scope="function")
#def valid_patient():
    #print("Creating patient")
    #return Patient(1001, "Aaron", 38, "Knee Replacement")

#testing all data
@pytest.mark.valid
def test_valid_patients(valid_patient):   #pass the fixture instead of values.
    assert PatientValidator.validate(valid_patient) is True

#testing name
@pytest.mark.valid
def test_valid_name(valid_patient):
    assert valid_patient.name == "Aaron"

#testing age
@pytest.mark.valid
def test_valid_age(valid_patient):
    assert valid_patient.age == 38

#invalid patient - moved this to conf test
#@pytest.fixture(scope="function")
#def invalid_patient():
    #return Patient(1002, "", 150, "Knee Replacement")

