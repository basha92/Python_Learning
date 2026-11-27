from patients import Patient
from validation import PatientValidator

def main():
    # 1. Patient input records

    records = [
        (1001, "Aaron", 38, "Knee Replacement"),
        (1002, "Kevin", 23, "Hip Implant"),
        ("1004", "Sami", 45, "Knee Replacement"),
        (1005, "", 52, "Knee Replacement"),
        (1006, "KK", 150, "Knee Replacement")
    ]


    # 2. Create and validate patient objects

    patients = []
    rejected = []

    for record in records:

        patient = Patient(*record)

        try:
            PatientValidator.validate(patient)
            patients.append(patient)

        except (ValueError, TypeError) as error:
            rejected.append(
                f"Patient record {record}: {error}"
            )

        print("Valid patients:", len(patients))
        print("Rejected patients:", len(rejected))

if __name__ == "__main__":
    main()