#Mini project: Patient Case File Setup
#Build a small test setup system that prepares a temporary patient case.
#Your tests should verify:
#- The folder is created.
#- The JSON file is created.
#- The JSON data can be read.
#- The patient ID and name are correct.
#- The temporary test resources are cleaned up by pytest.

import json
import pytest

#- The folder is created.
@pytest.fixture()
def patient_folder(tmp_path):
    # 1. SETUP (Before yield)
    print("\n[SETUP] Creating the patient folder...")
    folder = tmp_path / "patient_1001"
    folder.mkdir()

    # 2. PAUSE & HAND OVER (yield)
    yield folder

    # 3. TEARDOWN (After yield - runs after the test finishes!)
    print("\n[TEARDOWN] Test is over. Cleaning up...")

#- The JSON file is created.
@pytest.fixture()
def patient_json_file(patient_folder):
    print("\n[SETUP] Creating patient.json...")
    # 1. creating json file
    file_path = patient_folder / "patient.json"
    data = {"id": 1001, "name": "Alice"}
    # - Write patient information into it.
    file_path.write_text(json.dumps(data))

    # 2. PAUSE & HAND OVER (yield)
    yield file_path

    # 3. TEARDOWN (After yield - runs after the test finishes!)
    print("\n[TEARDOWN] JSON file fixture finished.")

def test_patient_json(patient_json_file):
    # Check that the file is really there
    assert patient_json_file.exists()

    # Read the file and check the name, ID
    content = json.loads(patient_json_file.read_text())
    assert content["name"] == "Alice"
    assert content["id"] == 1001