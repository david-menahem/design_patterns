from abc import ABC, abstractmethod

from abstract_factory.accessories_interfaces import Hat, Belt


class AccessoriesFactory(ABC):
    @abstractmethod
    def create_hat(self) -> Hat:
        pass

    @abstractmethod
    def create_belt(self) -> Belt:
        pass

