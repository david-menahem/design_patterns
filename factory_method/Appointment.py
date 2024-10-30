from abc import ABC, abstractmethod

from factory_method.clinic_service import ClinicService


class Appointment(ABC):

    @abstractmethod
    def create_clinic_service(self, **kwargs) -> ClinicService:
        pass

    def schedule_appointment(self, **kwargs):
        clinic_service = self.create_clinic_service(**kwargs)
        return clinic_service.schedule_appointment()

