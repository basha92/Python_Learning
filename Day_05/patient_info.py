#this is example of dictionary
#patient = {
#    "Name": "John",
#    "Age": 35,
#    "Height": 1.75,
#    "Weight": 72
#}

#printing each value
#print(patient.values())
#o/p: dict_values(['John', 35, 1.75, 72])

#creating list of patients
patients = [{"Name": "John", "Age": 35, "Height": 1.75, "Weight": 72},
            {"Name": "Jane", "Age": 32, "Height": 1.55, "Weight": 62},
            {"Name": "Mary", "Age": 28, "Height": 1.25, "Weight": 65},
            {"Name": "Laila", "Age": 26, "Height": 1.03, "Weight": 70},]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"

for patient in patients:
    bmi = calculate_bmi(patient["Weight"], patient["Height"])
    patient["BMI"] = round(bmi, 2)
    patient["Category"] = classify_bmi(bmi)

    # Print a simple report line with all fields
    print("--- Patient Report ---")
    print(f"Name: {patient['Name']}")
    print(f"Age: {patient['Age']}")
    print(f"Height: {patient['Height']} m")
    print(f"Weight: {patient['Weight']} kg")
    print(f"BMI: {patient['BMI']}")
    print(f"Classification: {patient['Category']}")
    print()