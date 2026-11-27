#Exercise 2: Setup and teardown

#Create a fixture called patient_folder.
#- Use tmp_path.
#- Create a folder named patient_1001.
#- Use yield to pass the folder to the test.
#- Print a setup message before yield.
#- Print a teardown message after yield.
#Write a test to check that the folder exists.

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

def test_folder_exists(patient_folder):
    assert patient_folder.exists()