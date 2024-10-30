from factory_method.blood_test_appointment import BloodTestAppointment
from factory_method.client_code import client_code
from factory_method.doctor_appointment import DoctorAppointment

if __name__ == '__main__':
    print("Doctor appointment")
    client_code(DoctorAppointment(), date="2024-12-31", location="Ra'anana", patient="Yael")
    print()
    print("Blood test appointment")
    client_code(BloodTestAppointment(), date="2024-11-30", location="Netanya",patient="David",
                test_type="blood cell count")
