#this file connects file handler and patient processor

from file_handler import find_json_files, read_json, write_json
from patient_processor import process_patient

def main():
    #file location
    files = find_json_files("Day_07/data")
    print(f"Found {len(files)} JSON file(s).")

    #finding files
    for file in files:
        print(f"Processing {file.name}...")
        patient = read_json(file)
        patient = process_patient(patient)
        write_json(file, patient)
        print(f"Saved {file.name} with BMI {patient['bmi']:.2f}.")

    print("Processing complete.")


if __name__ == "__main__":
    main()