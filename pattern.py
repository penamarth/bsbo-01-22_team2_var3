from abc import ABC, abstractmethod

# Observer Pattern Interfaces
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        print(f"{observer.__class__.__name__}: Подписан на уведомления")
        self.observers.append(observer)

    def detach(self, observer):
        print(f"{observer.__class__.__name__}: Отписан от уведомлений")
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


# Classes
class Patient(Observer):
    def __init__(self, name):
        self.name = name
        self.medical_record = None

    def make_appointment(self, schedule, date, time, doctor):
        print(f"Пациент {self.name}: Запрашиваю запись на {date}, {time} у {doctor}")
        schedule.make_appointment(date, time, doctor, self)

    def manage_record(self, schedule):
        print(f"Пациент {self.name}: Обращаюсь к расписанию для управления записью")
        schedule.manage_record(self)

    def update_personal_data(self, type_of_change, change):
        print(f"Пациент {self.name}: Обновляю личные данные: {type_of_change} -> {change}")

    def update(self, message):
        print(f"Пациент {self.name}: Получено уведомление - {message}")


class Doctor(Observer):
    def __init__(self, name):
        self.name = name
        self.appointments = []

    def get_available_time_slots(self, schedule):
        print(f"Врач {self.name}: Предоставляю доступные временные слоты")
        available_slots = ["10:00", "11:00"]
        schedule.drop_free_windows(available_slots)

    def add_appointment_doctor(self, appointment):
        print(f"Врач {self.name}: Добавляю запись к себе в расписание")
        self.appointments.append(appointment)

    def add_record_results(self, patient, results):
        print(f"Врач {self.name}: Ввожу результаты приема для пациента {patient.name}")
        if patient.medical_record is not None:
            patient.medical_record.update_medical_record(results)

    def update(self, message):
        print(f"Врач {self.name}: Получено уведомление - {message}")


class MedicalRecord(Subject):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient
        self.data = {}

    def update_medical_record(self, data):
        print(f"Медицинская карта: Обновляем данные карты пациента {self.patient.name}")
        self.data.update(data)
        self.notify(f"Медицинская карта обновлена: {data}")


class Appointment:
    def __init__(self, date, time, doctor):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = None

    def create_appointment_schedule(self, schedule, patient):
        print(f"Запись: Создаем новую запись в расписании на {self.date}, {self.time} у {self.doctor}")
        self.patient = patient
        schedule.create_appointment(self)


class Schedule(Subject):
    def __init__(self):
        super().__init__()
        self.appointments = []
        self.patients = []
        self.doctors = []

    def make_appointment(self, date, time, doctor, patient):
        print("Расписание: Получаем запрос на создание записи")
        appointment = Appointment(date, time, doctor)
        appointment.create_appointment_schedule(self, patient)

    def manage_record(self, patient):
        print("Расписание: Управляем записью пациента")

    def update_personal_data(self, patient, type_of_change, change):
        print("Расписание: Обновляем личные данные пациента")
        patient.update_personal_data(type_of_change, change)

    def get_available_time_slots(self, doctor):
        print("Расписание: Получаем доступные временные слоты у врача")
        doctor.get_available_time_slots(self)

    def drop_free_windows(self, time_slots):
        print(f"Расписание: Получили свободные временные слоты: {', '.join(time_slots)}")

    def create_appointment(self, appointment):
        print("Расписание: Создаем новую запись")
        self.appointments.append(appointment)
        self.notify(f"Запись создана: {appointment.date} {appointment.time} у {appointment.doctor}")


class SystemAdmin:
    def __init__(self):
        pass

    def manage_patients(self, patient_name):
        print(f"Администратор: Управляем пациентом {patient_name}")


# Прецедент 1
def presedent_1():
    patient = Patient("Иван Иванов")
    doctor = Doctor("Петр Петров")
    schedule = Schedule()
    schedule.doctors.append(doctor)

    schedule.attach(patient)
    schedule.attach(doctor)

    patient.make_appointment(schedule, "01-01-2023", "10:00", doctor.name)


# Прецедент 2
def presedent_2():
    patient = Patient("Иван Иванов")
    medical_record = MedicalRecord(patient)
    patient.medical_record = medical_record

    medical_record.attach(patient)

    doctor = Doctor("Петр Петров")
    medical_record.attach(doctor)

    doctor.add_record_results(patient, {"result": "Здоров"})


# Прецедент 3
def presedent_3():
    patient = Patient("Иван Иванов")
    doctor = Doctor("Петр Петров")
    schedule = Schedule()
    schedule.doctors.append(doctor)

    patient.manage_record(schedule)


# Прецедент 4
def presedent_4():
    patient = Patient("Иван Иванов")
    system_admin = SystemAdmin()
    schedule = Schedule()

    patient.update_personal_data("ФИО", "Иванов Иван Иванович")


if __name__ == "__main__":
    print("1.")
    presedent_1()
    print("2.")
    presedent_2()
    print("3.")
    presedent_3()
    print("4.")
    presedent_4()