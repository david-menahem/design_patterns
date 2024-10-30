from factory_method.clinic_service import ClinicService


class Doctor(ClinicService):

    def __init__(self, date, location, patient):
        self.date = date
        self.location = location
        self.patient = patient

    def schedule_appointment(self):
        return "Scheduled doctor appointment"
