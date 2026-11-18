#Exercise 4: CAD component classes
#Create a parent class called CADPart.
#Attributes:
#- Part number
#- Material
#- File path
#Create two child classes:
#- FemoralPart, with a condyle_type attribute.
#- TibialPart, with an insert_type attribute.
#Use super() and write a method to display each part's details.

class CadPart:
    def __init__(self, part_number, material, file_path):
        self.part_number = part_number
        self.material = material
        self.file_path = file_path

    def part(self):
        print (f"Part Number: {self.part_number}\n"
                f"Material: {self.material}\n"
                f"File Path: {self.file_path}")

class TibialPart(CadPart):
    def __init__(self,part_number, material, file_path, insert_type):
        super().__init__(part_number, material, file_path)
        self.insert_type = insert_type

    def part(self):
        print("\nTibial Part Details")
        super().part()
        print(f"Insert Type: {self.insert_type}")


class FemoralPart(CadPart):
    def __init__(self, part_number, material, file_path, condyle_type):
        super().__init__(part_number, material, file_path)
        self.condyle_type = condyle_type

    def part(self):
        print("\nFemoral Part Details")
        super().part()
        print(f"Condyle Type: {self.condyle_type}")

tibial1 = TibialPart(1001, "poly carbonate", "f:\\approved_docs\\cad\\tibial", "single")
tibial2 = TibialPart(1002, "poly propylene", "f:\\approved_docs\\cad\\tibial", "dual")
femoral = FemoralPart(1003, "fiber", "f:\\approved_docs\\cad\\femoral", "femoral")

tibial1.part()
tibial2.part()
femoral.part()

#Pattern to remember

#Parent prints → just call super().method().
#Parent returns → use it: return super().method() + "...", or store it first with base = super().part().