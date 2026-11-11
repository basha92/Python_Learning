import json
from pathlib import Path
from patient_details_class import Patient_Details

DATA_FILE = Path(__file__).parent / "data" / "patients.json"

def register_patients():
    patients = []
    records = [
        ("Asha Rao", 34, 1.65, 62 ),
        ("Ravi Kumar", 45, 1.72, 85),
        ("Meena Iyer", 29, 1.60, 50),
        ("Bad Data", -5, 1.70, 70),   # invalid on purpose, to test handling
    ]
    for rec in records:
        try:
            patients.append(Patient_Details(*rec))
        except ValueError as e:
            print(f"Skipped patient {rec[0]}: {e}")
    return patients

def display_patients(patients):
    print("\n--- Patient Records ---")
    for p in patients:
        print(p)


def save_patients(patients, filepath=DATA_FILE):
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in patients], f, indent=4)
        print(f"\nSaved {len(patients)} records to {filepath}")
    except OSError as e:
        print(f"Could not save file: {e}")


def main():
    patients = register_patients()
    display_patients(patients)
    save_patients(patients)


if __name__ == "__main__":
    main()