from cad_part import CADPart

class InsertPart(CADPart):
    def process(self):
        print("Processing Insert part")

    def validate(self):
        print("Validating Insert Part")
        
    def export(self):
        print("Exporting Insert Part")