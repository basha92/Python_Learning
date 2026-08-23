#this program reads and writes patient details
from pathlib import Path

def validate_name(name):
    """Returns (True, None) if valid, else (False, error_message)."""
    if not name or not name.replace(" ", "").isalpha():
        return False, "Invalid name"
    return True, None


def validate_age(age):
    if not age or not age.isdigit() or not (0 < int(age) <= 120):
        return False, "Invalid age"
    return True, None


def validate_height(height):
    if not height or not _is_valid_number(height) or float(height) <= 0:
        return False, "Invalid height"
    return True, None


def validate_weight(weight):
    if not weight or not _is_valid_number(weight) or float(weight) <= 0:
        return False, "Invalid weight"
    return True, None


def _is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#parsing through the file
#reading patient details from file
def parse_patient_file(file_path):
    """Reads the file and returns (True, data_dict) or (False, error_message)."""
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
    # checking file existence
    except FileNotFoundError:
        return False, "File not found"
    except PermissionError:
        return False, "Permission denied"

    # parsing file and stores to dictionary
    data = {}
    for line in content.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    return True, data
def read_patient_file(file_path):
    """
    Reads and validates a patient file using individual field validators.
    Returns (True, data_dict) on success, or (False, error_message) on failure.
    """
    ok, result = parse_patient_file(file_path)
    if not ok:
        return False, result

    data = result

    validators = [(validate_name, data.get("Name")),
                  (validate_age, data.get("Age")),
                  (validate_height, data.get("Height")),
                  (validate_weight, data.get("Weight"))]

    for validate_func, value in validators:
        is_valid, error = validate_func(value)
        if not is_valid:
            return False, error
    return True, data
#filepath = Path("Day_06/patient_register/patient_001.txt")
#read_patient_file(filepath)