#this file handles cad part attributes like number, material and the path

from abc import ABC, abstractmethod

class CadPart(ABC):
    def __init__(self, part_number, material, file_path):
        self.part_number = part_number
        self.material = material
        self.file_path = file_path

    def part(self):
        print (f"Part Number: {self.part_number}\n"
                f"Material: {self.material}\n"
                f"File Path: {self.file_path}")

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def export(self):
        pass


class TibialPart(CadPart):

    def validate(self):
        return "Tibial part validated"

    def process(self):
        return "Tibial part processed"

    def export(self):
        return "Tibial part exported"


class FemoralPart(CadPart):

    def validate(self):
        return "Femoral part validated"

    def process(self):
        return "Femoral part processed"

    def export(self):
        return "Femoral part exported"


class InsertPart(CadPart):

    def __init__(self, part_number, material, file_path, insert_type):
        super().__init__(part_number, material, file_path)
        self.insert_type = insert_type

    def validate(self):
        return "Insert part validated"

    def process(self):
        return "Insert part processed"

    def export(self):
        return "Insert part exported"