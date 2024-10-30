from abc import ABC, abstractmethod


class ClinicService(ABC):

    @abstractmethod
    def schedule_appointment(self):
        pass

