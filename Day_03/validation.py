# This file validates the user input for the BMI calculator.
from pathlib import Path
import re
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from Day_02.bmi_calculator import calculate_bmi


def is_positive(value):
    """Return True if the value is a number greater than zero."""
    return isinstance(value, (int, float)) and value > 0


def is_valid_height(height):
    """Return True if the height is positive and realistic for BMI calculation."""
    return is_positive(height) and 0.5 <= height <= 2.5


def is_valid_weight(weight):
    """Return True if the weight is positive and realistic for BMI calculation."""
    return is_positive(weight) and 2 <= weight <= 500

def is_valid_name(name):
    """Return True if the name contains only letters and spaces."""
    return (
        isinstance(name, str)
        and bool(name.strip())
        and bool(re.fullmatch(r"[A-Za-z ]+", name.strip()))
    )

def main():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if  is_valid_weight(weight) and is_valid_height(height):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
    else:
        print("Please enter a valid weight and height.")
    if not is_valid_name(name):
        print("Please enter a valid name.")

if __name__ == "__main__":
    main()