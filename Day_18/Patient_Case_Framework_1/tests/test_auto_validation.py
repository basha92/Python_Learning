import json
import pytest
from patients import Patient
from validation import PatientValidator

@pytest.fixture
def patient_folder(tmp_path):
    folder = tmp_path / "patients_data"
    folder.mkdir()
    yield folder

@pytest.fixture
def patient_json_file(patient_folder):
    file_path = patient_folder / "patient.json"

    patients = [
        Patient(1001, "Aaron", 38, "Knee Replacement"),
        Patient(1002, "Maya", 45, "Hip Replacement"),
        Patient(1003, "Liam", 29, "ACL Repair"),
    ]

    patients_data = [p.__dict__ for p in patients]
    file_path.write_text(json.dumps(patients_data, indent=4))

    print(f"\nJSON File Location: {file_path}")

    yield file_path

# AUTOUSE FIXTURE: Runs automatically before every test!
@pytest.fixture(autouse=True)
def auto_validate_patients(patient_json_file):
    print("\n[AUTOUSE] Automatically validating all patients in JSON...")
    content = json.loads(patient_json_file.read_text())

    for item in content:
        # Rebuild Patient object and validate it before any test runs
        patient = Patient(**item)
        PatientValidator.validate(patient)

    yield
    print("\n[AUTOUSE] Test finished, validation check complete.")

# Notice: Neither test asks for 'auto_validate_patients', yet it runs for BOTH!
def test_patient_count(patient_json_file):
    content = json.loads(patient_json_file.read_text())
    assert len(content) == 3

def test_first_patient_name(patient_json_file):
    content = json.loads(patient_json_file.read_text())
    assert content[0] ["name"] == "Aaron"
