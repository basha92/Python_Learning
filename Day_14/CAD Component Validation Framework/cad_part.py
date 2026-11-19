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