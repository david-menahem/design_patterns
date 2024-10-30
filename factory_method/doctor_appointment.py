from factory_method.Appointment import Appointment
from factory_method.clinic_service import ClinicService
from factory_method.doctor import Doctor


class DoctorAppointment(Appointment):
    def create_clinic_service(self, date, location, patient) -> ClinicService:
        return Doctor(date, location, patient)

