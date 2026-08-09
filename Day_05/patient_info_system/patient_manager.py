#this program collects the patient info and stores it into list of dictionaries.
#importing bmi functionality
from bmi import calculate_bmi
from validation import validate_name, validate_age, validate_weight, validate_height, get_valid_input

# Step 1: Initialize an empty list to store the dictionaries
patients = []

#defining required functions
def add_patient():
    # Step 2: Prompt user for individual data fields
    name = get_valid_input("\nEnter Patient Name: ", str, validate_name)
    age = get_valid_input("Enter Patient Age: ", int, validate_age)
    height = get_valid_input("Enter Patient Height(in Meters): ", float, validate_height)
    weight = get_valid_input("Enter Patient Weight(inKGs): ", float, validate_weight)
    bmi = calculate_bmi(weight, height)

    # Step 3: Create a dictionary containing the current input
    patient = {
        "Name": name,
        "Age": age,
        "Weight": weight,
        "Height": height,
        "BMI": bmi
    }
    patients.append(patient)
    print("Patient Added!")

def view_patients():
    if not patients:
        print("No patients yet.")
        return
    print("----List of Patients----")
    for patient in patients:
        print(f"Name: {patient['Name']}, Age: {patient['Age']}, Height: {patient['Height']} m, Weight: {patient['Weight']} kg, BMI: {patient['BMI']}")

def search_patient():
    name = input("Enter the name to search: ")
    for patient in patients:
        if patient["Name"].lower() == name.lower():
            print(f"Name: {patient['Name']}, Age: {patient['Age']}, Height: {patient['Height']} m, Weight: {patient['Weight']} kg, BMI: {patient['BMI']}")
        else:
            print("Patient not found")
        