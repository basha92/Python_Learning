from cadpart import TibialPart, FemoralPart
from surgical_patient import SurgicalPatient

patient1 = SurgicalPatient("P1001", "Arun", 52, "Knee Replacement")
patient2 = SurgicalPatient("P1002", "Kumar", 40, "Hip Implant")

tibial1 = TibialPart(1001, "poly carbonate", "f:\\approved_docs\\cad\\tibial", "single")
tibial2 = TibialPart(1002, "poly propylene", "f:\\approved_docs\\cad\\tibial", "dual")
femoral = FemoralPart(1003, "fiber", "f:\\approved_docs\\cad\\femoral", "femoral")

patient1.display_details()
patient2.display_details()
tibial1.part()
tibial2.part()
femoral.part()