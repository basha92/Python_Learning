from tibial import TibialPart
from femoral import FemoralPart
from insert import InsertPart

def process_cad_part(part):
    part.process()


parts = [TibialPart(), FemoralPart(), InsertPart()]

for part in parts:
    process_cad_part(part)