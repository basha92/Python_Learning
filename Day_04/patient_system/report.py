#displays patient details

def display_patient_summary(name, age, height, weight, bmi):
    print("\n=== Patient Summary ===")
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Height : {height} m")
    print(f"Weight : {weight} kg")
    print(f"BMI    : {bmi:.2f}")