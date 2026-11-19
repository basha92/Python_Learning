from cad_part import CADPart

class FemoralPart(CADPart):
    def process(self):
        print("Processing Femoral part")

    def validate(self):
        print("Validating Femoral Part")
        
    def export(self):
        print("Exporting Femoral Part")