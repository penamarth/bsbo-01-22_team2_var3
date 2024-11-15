```plantuml
@startuml class_diagram
package "Clinic Information System" {

    class Patient {
        + name : String
        + birthDate : Date
        + address : String
        + medicalRecord : MedicalRecord
        + makeAppointment()
        + viewMedicalRecord()
        + manageRecord()
    }

    class Doctor {
        + name : String
        + specialty : String
        + schedule : Schedule
        + patients : List<Patient>
        + appointmrnt : List<Appointment>
        + recordVisit()
        + updateMedicalRecord()
    }

    class MedicalRecord {
        + diagnosis : String
        + visitHistory : List<Visit>
        + addVisit()
        + updateRecord()
        + rewriteRecord()
        + viewRecord()
    }

    class Visit {
        + date : Date
        + doctor : Doctor
        + notes : String
    }

    class Appointment {
        + date : Date
        + time : Time
        + patient : Patient
        + doctor : Doctor
        + createAppointment()
        + cancelAppointment()
        + changeAppointment()
    }

    class Schedule {
        + doctor : List<Doctor>
        + appointments : List<Appointment>
        + updateSchedule()
        + getAvailableTimeSlots()
    }

    class SystemAdmin {
        + managePatients()
        + manageSchedules()
    }

    class Register {
        + name : String
        + registerPatient()
        + updateAppointment()
    }

    Patient "1" -- "many" MedicalRecord : has
    Doctor "1" -- "many" MedicalRecord : has
    Doctor "1" -- "many" Patient : attends
    
    Doctor "1" -- "many" Visit : conducts
    MedicalRecord "1" -- "many" Visit : contains
    Doctor "1" -- "1" Schedule : has
    Appointment "1" -- "1" Patient : schedules
    Appointment "many" -- "1" Doctor : schedules
    Schedule "1" -- "many" Appointment : includes
    Register "1" -- "many" Appointment : manages
    Register "1" -- "many" Patient : registers
    
    SystemAdmin "1" -- "many" Patient : manages 
    SystemAdmin "1" -- "many" Schedule : manages  

}
@enduml
```
