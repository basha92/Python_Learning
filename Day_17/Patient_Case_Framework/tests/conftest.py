import pytest

from patients import Patient


#fixing the input
@pytest.fixture(scope="function")
def valid_patient():
    print("Creating patient")
    return Patient(1001, "Aaron", 38, "Knee Replacement")

#invalid patient
@pytest.fixture(scope="function")
def invalid_patient():
    return Patient(1002, "", 150, "Knee Replacement")

# Use params inside @pytest.fixture instead of @pytest.mark.parametrize
@pytest.fixture(params=['1001', 10.5, ""])
def patient_with_invalid_id(request):
    return Patient(request.param, "Sami", 45, "Knee Replacement")

@pytest.fixture(params=[0, -1, 121, 150])
def patient_with_invalid_age(request):
    return Patient(1006, "KK", request.param, "Knee Replacement")

@pytest.fixture(params=["", "   ", None])
def patient_with_invalid_surgery(request):
    return Patient(1001, "Aaron", 38, request.param)