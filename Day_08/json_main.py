#this is example of patient registry
from pathlib import Path
from Day_08.json_validation import read_patient_file

def main():
    patient_dir = Path("Day_07/data")
    patient_files = sorted(patient_dir.glob("patient_*.json"))

    #variables for process count
    processed = 0
    failed = 0
    errors = []  # list of (filename, error_message)

    for file_path in patient_files:
        success, result = read_patient_file(file_path)
        if success:
            processed += 1
        else:
            failed += 1
            errors.append((file_path.name, result))

    print_summary(len(patient_files), processed, failed, errors)


def print_summary(files_found, processed, failed, errors):
    file_path = "Day_07/data/output.txt"
    #with open(file_path,"w") as file:
        #file.write()
    print("=" * 32)
    print("Patient Processing Summary")
    print("=" * 32)
    print(f"Files Found : {files_found}")
    print(f"Processed   : {processed}")
    print(f"Failed      : {failed}")

    if errors:
        print("Errors:")
        for filename, message in errors:
            print(f" - {filename} : {message}")


if __name__ == "__main__":
    main()