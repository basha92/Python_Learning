#Exercise 1: Create an abstract class
#Create CADPart using ABC. Add an abstract method called process(). Implement it in TibialPart and FemoralPart.

#Exercise 2: Multiple abstract methods
#Add validate() and export() as abstract methods. Implement all three methods in TibialPart.

#Exercise 3: Test enforcement
#Create a child class that implements process() but skips export(). Try creating an object. Observe the error.
#error message:
#TypeError: Can't instantiate abstract class TibialPart without an implementation for abstract methods 'export', 'validate'

from abc import ABC, abstractmethod

class CADPart(ABC):

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def export(self):
        pass

class TibialPart(CADPart):
    def process(self):
        print("Processing Tibial Part")

    def validate(self):
        print("Processing Tibial Part")

    def export(self):
        print("Processing Tibial Part")
    

class FemoralPart(CADPart):
    def process(self):
            print("Processing Femoral Part")

parts = [TibialPart()]  #ex2 didn't give error because fem part is not added in the list.

for part in parts:
     part.process()