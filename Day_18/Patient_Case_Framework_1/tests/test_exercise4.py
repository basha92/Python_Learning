import pytest

# Runs ONCE for the whole file
@pytest.fixture(scope="module")
def hospital_database():
    print("\n>>> [MODULE SETUP] Connecting to Hospital Database ONCE <<<")
    yield "DB_CONNECTION"
    print("\n>>> [MODULE TEARDOWN] Closing Hospital Database <<<")

# Runs BEFORE EVERY test automatically (autouse=True)
@pytest.fixture(scope="function", autouse=True)
def clean_desk():
    print("\n--- [FUNCTION SETUP] Wiping desk clean before test ---")
    yield
    print("\n--- [FUNCTION TEARDOWN] Wiping desk clean after test ---")

def test_one(hospital_database):
    print("Running Test 1...")
    assert hospital_database == "DB_CONNECTION"

def test_two(hospital_database):
    print("Running Test 2...")
    assert hospital_database == "DB_CONNECTION"