#this program contains patient report functions.
def name(patient_name):
    '''check if the name is valid string'''
    if patient_name.isalpha():
        return patient_name
    else:
        raise ValueError("Invalid patient name")
def age(patient_age):
    if patient_age.isdigit()and int(patient_age) > 0:
        return int(patient_age)
    else:
        raise ValueError("Invalid patient age")
def height(patient_height):
    try:
        value = float(patient_height)
    except ValueError:
        raise ValueError("Invalid patient height")
    if value > 0 and value < 3:
        return value
    raise ValueError("Invalid patient height")

def weight(patient_weight):
    try:
        value = float(patient_weight)
    except ValueError:
        raise ValueError("Invalid patient weight")
    if value > 0:
        return value
    raise ValueError("Invalid patient weight")
def BMI(patient_weight, patient_height):
    return patient_weight / (patient_height ** 2)