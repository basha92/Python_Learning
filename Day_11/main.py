from patient import Patient

def display_details(patient):
    print("\n--- Patient Record ---")
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Height: {patient.height}")
    print(f"BMI: {patient.bmi}")
    print(f"Name: {patient.bmi_category}")

def main():
    #1. create a valid patient
    try:
        p1 = Patient("Arun", 31, 70, 175)
    except (ValueError, TypeError) as e:
        print("Error: ", e)
        return
    display_details(p1)

    # 2. Update weight and show new BMI
    p1.weight = 85
    print("\nAfter weight update:")
    display_details(p1)

    # 3. Try invalid data
    records = [("Ravi", 150, 60, 170),
               ("Sam", 25, -5, 170),
               ("", 25, 60, 170)]

    for rec in records:
        try:
            Patient(*rec)
        except ValueError as e:
            print(f"Skipped patient {rec[0]}: {e}")

if __name__ == "__main__":
    main()