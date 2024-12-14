class Patient:
    def __init__(self, name, birth_date, address):
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.medical_record = MedicalRecord(self)

    def update_personal_data(self, field, value):
        setattr(self, field, value)
        print(f"[Patient.update_personal_data] Обновлены данные: {field} -> {value}")


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.schedule = []

    def add_appointment(self, appointment):
        self.schedule.append(appointment)
        print(f"[Doctor.add_appointment] Добавлена запись: {appointment.date} {appointment.time}")


class MedicalRecord:
    def __init__(self, patient):
        self.patient = patient
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        print(f"[MedicalRecord.add_record] Добавлена запись: {record}")

    def update_record(self, record):
        self.records[-1] = record
        print(f"[MedicalRecord.update_record] Запись обновлена: {record}")


class Appointment:
    def __init__(self, date, time, doctor, patient):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient


class Schedule:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def log(self, method_name, details):
        print(f"[Schedule.{method_name}] {details}")

    def add_doctor(self, name, specialty):
        doctor = Doctor(name, specialty)
        self.doctors.append(doctor)
        self.log("add_doctor", f"Добавлен врач {name}, специализация: {specialty}")

    def register_patient(self, name, birth_date, address):
        patient = Patient(name, birth_date, address)
        self.patients.append(patient)
        self.log("register_patient", f"Зарегистрирован пациент {name}")

    def make_appointment(self, patient_name, doctor_name, date, time):
        self.log("make_appointment", f"Создание записи: пациент={patient_name}, врач={doctor_name}, дата={date}, время={time}")
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)

        if not patient or not doctor:
            print(f"[Schedule.make_appointment] Ошибка: пациент или врач не найден")
            return

        appointment = Appointment(date, time, doctor, patient)
        self.appointments.append(appointment)
        doctor.add_appointment(appointment)
        self.log("make_appointment", f"Запись создана: {patient.name} -> {doctor.name} на {date} {time}")

    def update_medical_record(self, patient_name, record):
        self.log("update_medical_record", f"Обновление медкарты: пациент={patient_name}, запись={record}")
        patient = next((p for p in self.patients if p.name == patient_name), None)

        if not patient:
            print(f"[Schedule.update_medical_record] Пациент {patient_name} не найден")
            return

        patient.medical_record.add_record(record)

    def update_personal_data(self, patient_name, field, value):
        self.log("update_personal_data", f"Обновление данных пациента: {patient_name}, {field} -> {value}")
        patient = next((p for p in self.patients if p.name == patient_name), None)

        if not patient:
            print(f"[Schedule.update_personal_data] Пациент {patient_name} не найден")
            return

        patient.update_personal_data(field, value)


# Прецеденты

def presedent_1(schedule):
    schedule.log("presedent_1", "Начало прецедента")
    schedule.register_patient("Иван Иванов", "01-01-1990", "ул. Ленина, д. 1")
    schedule.add_doctor("Петр Петров", "Терапевт")
    schedule.make_appointment("Иван Иванов", "Петр Петров", "01-01-2023", "10:00")
    schedule.log("presedent_1", "Конец прецедента")

def presedent_2(schedule):
    schedule.log("presedent_2", "Начало прецедента")
    schedule.register_patient("Иван Иванов", "01-01-1990", "ул. Ленина, д. 1")
    schedule.update_medical_record("Иван Иванов", "Обследование: Здоров")
    schedule.log("presedent_2", "Конец прецедента")

def presedent_3(schedule):
    schedule.log("presedent_3", "Начало прецедента")
    schedule.register_patient("Иван Иванов", "01-01-1990", "ул. Ленина, д. 1")
    schedule.update_medical_record("Иван Иванов", "Результаты анализов: Отклонений нет")
    schedule.log("presedent_3", "Конец прецедента")

def presedent_4(schedule):
    schedule.log("presedent_4", "Начало прецедента")
    schedule.register_patient("Иван Иванов", "01-01-1990", "ул. Ленина, д. 1")
    schedule.update_personal_data("Иван Иванов", "address", "ул. Советская, д. 2")
    schedule.log("presedent_4", "Конец прецедента")


if __name__ == "__main__":
    schedule = Schedule()

    print("1.")
    presedent_1(schedule)
    print("2.")
    presedent_2(schedule)
    print("3.")
    presedent_3(schedule)
    print("4.")
    presedent_4(schedule)
