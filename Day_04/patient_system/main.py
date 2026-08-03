#this program calls for the all functions created for patient system
from patient import get_patient_details
from validation import (
    validate_name,
    validate_age,
    validate_height,
    validate_weight,
)
from report import display_patient_summary

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    try:
        #collect patient details
        name, age, height, weight = get_patient_details()

        #validating the inputs
        name = validate_name(name)
        age = validate_age(age)
        height = validate_height(height)
        weight = validate_weight(weight)

        #calculating BMI
        bmi = calculate_bmi(weight, height)

        #reporting
        display_patient_summary(name, age, height, weight , bmi)
        
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()