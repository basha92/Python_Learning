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