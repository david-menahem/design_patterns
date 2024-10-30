from factory_method.Appointment import Appointment


def client_code(appointment: Appointment, **kwargs):
    print(appointment.schedule_appointment(**kwargs))



