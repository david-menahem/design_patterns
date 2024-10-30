from factory_method.Appointment import Appointment
from factory_method.bood_test import BloodTest
from factory_method.clinic_service import ClinicService


class BloodTestAppointment(Appointment):
    def create_clinic_service(self, date, location, patient, test_type) -> ClinicService:
        return BloodTest(date, location, patient, test_type)



