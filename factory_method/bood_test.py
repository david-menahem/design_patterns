from factory_method.clinic_service import ClinicService


class BloodTest(ClinicService):

    def __init__(self, date, location, patient, test_type):
        self.data = date
        self.location = location
        self.patient = patient
        self.test_type = test_type

    def schedule_appointment(self):
        return "Scheduled blood test"

