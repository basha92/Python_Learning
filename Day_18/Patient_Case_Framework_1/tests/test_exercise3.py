#Exercise 3: Create a JSON file


#Extend your folder fixture or create another fixture.
#- Create patient.json inside the temporary folder.
#- Write patient information into it.
#- Use yield to provide the file path.
#- In the test, check that the file exists.
#- Read the JSON and check the patient's name.

import json
import pytest

@pytest.fixture
def patient_folder(tmp_path):
    # 1. SETUP (Before yield)
    print("\n[SETUP] Creating the patient folder...")
    folder = tmp_path / "patient_1001"
    folder.mkdir()

    # 2. PAUSE & HAND OVER (yield)
    yield folder

    # 3. TEARDOWN (After yield - runs after the test finishes!)
    print("\n[TEARDOWN] Test is over. Cleaning up...")

@pytest.fixture
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

    # Read the file and check the name
    content = json.loads(patient_json_file.read_text())
    assert content["name"] == "Alice"