class Patient:
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


class Doctor:
    def __init__(self, name):
        self.name = name
        self.appointments = []

    def get_available_time_slots(self, schedule):
        print(f"Врач {self.name}: Предоставляю доступные временные слоты")
        # Здесь можно реализовать логику получения свободных временных слотов
        available_slots = ["10:00", "11:00"]
        schedule.drop_free_windows(available_slots)

    def add_appointment_doctor(self, appointment):
        print(f"Врач {self.name}: Добавляю запись к себе в расписание")
        self.appointments.append(appointment)

    def add_record_results(self, patient, results):
        print(f"Врач {self.name}: Ввожу результаты приема для пациента {patient.name}")
        if patient.medical_record is not None:
            patient.medical_record.update_medical_record(results)


class MedicalRecord:
    def __init__(self, patient):
        self.patient = patient
        self.data = {}

    def update_medical_record(self, data):
        print(f"Медицинская карта: Обновляем данные карты пациента {self.patient.name}")
        self.data.update(data)
        self.alert(True)

    def alert(self, is_ok):
        print("Медицинская карта: Уведомление об успешном обновлении данных")


class Appointment:
    def __init__(self, date, time, doctor):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = None

    def create_appointment_schedule(self, schedule, patient):
        print(f"Запись: Создаем новую запись в расписании на {self.date}, {self.time} у {self.doctor}")
        self.patient = patient  # Устанавливаем пациента для этой записи
        schedule.create_appointment(self)

    def alert_appointment(self):
        print(f"Запись: Уведомляем пациента {self.patient.name} о создании записи")


class Schedule:
    def __init__(self):
        self.appointments = []
        self.patients = []
        self.doctors = []

    def make_appointment(self, date, time, doctor, patient):
        print("Расписание: Получаем запрос на создание записи")
        appointment = Appointment(date, time, doctor)
        appointment.create_appointment_schedule(self, patient)

    def manage_record(self, patient):
        print("Расписание: Управляем записью пациента")
        # Логика управления записью пациента

    def update_personal_data(self, patient, type_of_change, change):
        print("Расписание: Обновляем личные данные пациента")
        # Логика обновления личных данных пациента
        patient.update_personal_data(type_of_change, change)

    def get_available_time_slots(self, doctor):
        print("Расписание: Получаем доступные временные слоты у врача")
        doctor.get_available_time_slots(self)

    def drop_free_windows(self, time_slots):
        print(f"Расписание: Получили свободные временные слоты: {', '.join(time_slots)}")

    def create_appointment(self, appointment):
        print("Расписание: Создаем новую запись")
        self.appointments.append(appointment)
        appointment.alert_appointment()

    def drop_appointment_schedule(self, patient, date, time, doctor):
        print("Расписание: Удаляем старую запись")
        # Логика удаления старой записи

    def add_appointment_doctor(self, date, time, doctor):
        print("Расписание: Добавляем запись к доктору")
        for doc in self.doctors:
            if doc.name == doctor:
                doc.add_appointment_doctor(Appointment(date, time, doctor))


class SystemAdmin:
    def __init__(self):
        pass

    def manage_patients(self, patient_name):
        print(f"Администратор: Управляем пациентом {patient_name}")
        # Логика управления пациентом


# Прецедент 1
def presedent_1():
    patient = Patient("Иван Иванов")
    doctor = Doctor("Петр Петров")
    schedule = Schedule()
    schedule.doctors.append(doctor)

    patient.make_appointment(schedule, "01-01-2023", "10:00", doctor.name)


# Прецедент 2
def presedent_2():
    patient = Patient("Иван Иванов")
    medical_record = MedicalRecord(patient)
    patient.medical_record = medical_record
    doctor = Doctor("Петр Петров")
    schedule = Schedule()
    schedule.doctors.append(doctor)

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