#Polymorphism = Greek word that means to "have many forms or faces"
#Poly = Many
#Morphe = Form

#TWO WAYS TO ACHIEVE POLYMORPHISM
#1. Inheritance = An object could be treated of the same type as a parent class
#2. "Duck typing" = Object must have necessary attributes/methods

#Exercise1: Create a parent class CADPart with a method calculate_volume(). 
#Override it in TibialPart and FemoralPart to return different values.

'''class CADPart:
    #def __init__(self, volume):
       # self.volume = volume

    def calculate_volume(self):
        pass

class TibialPart(CADPart):
    def calculate_volume(self):
        return 210

class FemoralPart(CADPart):
    def calculate_volume(self):
        return 150

parts = [TibialPart(), FemoralPart()]

for part in parts:
    print(part.calculate_volume())'''

#Exercise 2: Polymorphism
#Create three CAD part objects and call display_details() through a single loop.

'''class TibialPart:
    def display_details(self):
        print("This is Tibial Part")

class FemoralPart:
    def display_details(self):
        print("This is Femoral Part")

class InsertPart:
    def display_details(self):
        print("This is Insert Part")

parts = [TibialPart(), FemoralPart(), InsertPart()]
for part in parts:
    part.display_details()'''

#Exercise 3: Duck typing
#Create a function named export_part(part). It should call part.export(). Create two different classes with their own export() methods.

class TibialPart:
    def export(self):
        print("Exporting tibial part")


class FemoralPart:
    def export(self):
        print("Exporting femoral part")


class InsertPart:
    def export(self):
        print("Exporting insert part")

# 1. Helper Function: Acts as a single interface to trigger the .export() method on any given object.
def export_part(part):
    part.export()

# 2. Part List: Creates instances (objects) of each implant class and stores them together in one list.
parts = [TibialPart(), FemoralPart(), InsertPart()]

# 3. Calling / Execution: Loops through the list and calls export_part() on each item one by one.
for part in parts:
    export_part(part)