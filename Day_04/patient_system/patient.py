
def get_patient_details():
    #takes user input for name, age, height, weight.
    name = str(input("Enter Patient Name: "))
    age = int(input("Enter patient Age: "))
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    return name, age, height, weight