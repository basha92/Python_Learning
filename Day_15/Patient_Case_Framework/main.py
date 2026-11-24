#this file connects all the details here.

from pathlib import Path

from patients import Patient
from validation import PatientValidator
from cad_part import TibialPart, FemoralPart, InsertPart
from cad_processor import CADProcessor
from report import Report
from file_manager import FileManager


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


# 3. Create CAD part objects

parts = [
    TibialPart(1001, "Polycarbonate", "CAD/Tibial"),
    FemoralPart(1002, "Titanium", "CAD/Femoral"),
    InsertPart(1003, "Polyethylene", "CAD/Insert", "Single")
]


# 4. Process CAD parts

processor = CADProcessor()
cad_results = processor.process_parts(parts)


# 5. Prepare patient data file content

patient_content = "\n".join(
    f"ID: {p.patient_id}, Name: {p.name}, "
    f"Age: {p.age}, Surgery: {p.surgery_type}"
    for p in patients
)


# 6. Generate final report

report_content = Report.build(
    patients,
    cad_results,
    rejected
)


# 7. Write both files

base_path = Path(__file__).resolve().parent

patient_file = base_path / "data" / "patients.txt"
report_file = base_path / "output" / "patient_report.txt"

FileManager.write_report(patient_file, patient_content)
FileManager.write_report(report_file, report_content)

print("Valid patients:", len(patients))
print("Rejected patients:", len(rejected))

print("\nPatient content:")
print(repr(patient_content))

print("\nReport content:")
print(repr(report_content))

print("\nPatient file location:", patient_file.resolve())
print("Report file location:", report_file.resolve())


print("Patient data saved successfully.")
print("Patient report generated successfully.")


print("\n--- Reading back from disk ---")
print(patient_file.read_text(encoding="utf-8"))
print("Size in bytes:", patient_file.stat().st_size)
