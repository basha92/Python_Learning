#a logger is a tool to record messages frpm your program while it runs, which can help you debug, monitor and maintain your code effectively.
#its part of python's logging module
#|Level       | Purpose
#|------------|---------------------------------
#|DEBUG       |Detailed information (mainly foro dev)
#|INFO        |General Info
#|WARNING     |Something go wrong but didn't affect
#|ERROR       |Something go wrong and affects other features
#|CRITICAL    |Serious error (app crash)
#

import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="process.log",
    filemode="a"
)


def validate_name(name):
    """Validate the patient's name."""
    logging.info("Validating name")

    if not isinstance(name, str) or not name.strip():
        logging.error("Invalid name")
        return False, "Name is required"

    if not name.replace(" ", "").isalpha():
        logging.error("Invalid name")
        return False, "Name must contain letters and spaces only"

    return True, None


def validate_age(age):
    logging.info("Validating age")

    if age is None:
        logging.error("Invalid age")
        return False, "Age is required"

    age = str(age)

    if not age.isdigit() or not (0 < int(age) <= 120):
        logging.error("Invalid age")
        return False, "Age must be between 1 and 120"

    return True, None


def _is_valid_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def validate_height(height):
    logging.info("Validating height")

    if (
        height is None
        or not _is_valid_number(height)
        or float(height) <= 0
    ):
        logging.error("Invalid height")
        return False, "Height must be a positive number"

    return True, None


def validate_weight(weight):
    logging.info("Validating weight")

    if (
        weight is None
        or not _is_valid_number(weight)
        or float(weight) <= 0
    ):
        logging.error("Invalid weight")
        return False, "Weight must be a positive number"

    return True, None


def parse_patient_file(file_path):
    """Read JSON data from the patient file."""

    try:
        with open(file_path, "r") as file:
            content = json.load(file)

    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        return False, "File not found"

    except PermissionError:
        logging.error("Permission denied: %s", file_path)
        return False, "Permission denied"

    except json.JSONDecodeError:
        logging.error("Invalid JSON: %s", file_path)
        return False, "Invalid JSON"

    return True, content


def read_patient_file(file_path):
    """Read and validate patient data."""

    ok, result = parse_patient_file(file_path)

    if not ok:
        return False, result

    data = result

    if not isinstance(data, dict):
        logging.error("Patient data must be a JSON object")
        return False, "Patient data must be a JSON object"

    validators = [
        (validate_name, data.get("name")),
        (validate_age, data.get("age")),
        (validate_height, data.get("height")),
        (validate_weight, data.get("weight"))
    ]

    for validate_func, value in validators:
        is_valid, error = validate_func(value)

        if not is_valid:
            logging.error("Patient validation failed: %s", error)
            return False, error

    logging.info("Patient file validated successfully")
    return True, data


filepath = "Day_07/data/patient_002.json"

ok, result = read_patient_file(filepath)

if ok:
    print("Patient data is valid:", result)
else:
    print("Validation failed:", result)
