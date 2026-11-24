#this file displays patient details, cad part details and processing details.

class Report:

    @staticmethod
    def build(patients, cad_results, rejected):

        lines = ["===== PATIENT CASE REPORT ====="]

        for patient in patients:
            lines.append(
                f"\nPatient ID: {patient.patient_id}"
            )
            lines.append(f"Name: {patient.name}")
            lines.append(f"Age: {patient.age}")
            lines.append(f"Surgery: {patient.surgery_type}")

        lines.append("\n===== CAD PROCESSING =====")

        lines.extend(cad_results)

        lines.append("\n===== REJECTED PATIENTS =====")

        lines.extend(rejected if rejected else ["None"])

        return "\n".join(lines)