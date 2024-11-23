@startuml sequence_diagram_2

actor SystemAdmin
participant Patient
actor Patient_Person

Patient -> SystemAdmin: Класс пациент запрашивает изменение своих данных updatePersonalData(data)
SystemAdmin ->  Patient: Администратор обращается к классу пациент и выбирает конкретного пациента managePatients(patient_name)
SystemAdmin -> Patient: Администратор вносит изменения в профиль пациента managePatients(patient_name) -> old_data = new_data
Patient -> SystemAdmin: Класс пациент уведомляет администратора об изменениях IsUpdateOk(is_ok)
Patient -> Patient_Person: Класс пациент уведомляет пациента об изменениях alarmPatient(is_ok_message)


@enduml
