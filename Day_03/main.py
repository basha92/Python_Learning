#this acts as main file for patient report record.
from report import name, age, height, weight, BMI
def main():
    patient_name = name(input("Enter Patient Name: "))
    patient_age = age(input("Enter Patient Age: "))
    patient_height = height(input("Enter Patient Height in meters: "))
    patient_weight = weight(input("Enter Patient Weight in kg: "))

    #calling bmi function
    bmi = BMI(weight(patient_weight), height(patient_height))

    #calling other functions to print the report
    print("===================")
    print("Patient Summary")
    print("===================")
    print(f"Name: {name(patient_name)}")
    print(f"Age: {age(patient_age)}")
    print(f"Height: {height(patient_height)}")
    print(f"Weight: {weight(patient_weight)}")
    print(f"BMI: {bmi:.2f}")
    print("===================")

if __name__ == "__main__":
    main()