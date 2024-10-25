from abc import ABC, abstractmethod


class Hat(ABC):
    @abstractmethod
    def wear(self):
        pass


class Belt(ABC):
    @abstractmethod
    def wear(self):
        print("w")
        pass
