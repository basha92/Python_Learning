from tibial import TibialPart
from femoral import FemoralPart
from insert import InsertPart

parts = [TibialPart(), FemoralPart(), InsertPart()]

for part in parts:
    part.process()
    part.validate()
    part.export()