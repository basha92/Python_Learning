#this program does the following: calculate_bmi()  process_patient()

def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def process_patient(patient):
    weight = patient["weight"]
    height = patient["height"]

    bmi = calculate_bmi(height, weight)
    patient["bmi"] = bmi

    return patient