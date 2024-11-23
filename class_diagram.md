@startuml class_diagram
package "Clinic Information System" {

    class Patient {
        + name : String
        + birthDate : Date
        + address : String
        + medicalCard : MedicalRecord
        + makeAppointment()
        + viewMedicalRecord()
        + manageRecord()
        + updatemedicalCard()
        + updatePersonalData()
        + alarmPatient()
        + IsUpdateOk()
    }

    class Doctor {
        + name : String
        + specialty : String
        + schedule : Schedule
        + patients : List<Patient>
        + appointment : List<Appointment>
        + recordVisit()
        + updateMedicalRecord()
        + dropFreeWindows()
    }

    class MedicalRecord {
        + diagnosis : String
        + visitHistory : List<Visit>
        + addRecord()
        + updateRecord()
        + rewriteRecord()
        + viewRecord()
        + message()
    }


    class Appointment {
        + date : Date
        + time : Time
        + patient : Patient
        + doctor : Doctor
        + createAppointment()
        + cancelAppointment()
        + changeAppointment()
        + alertAppointment()
    }

    class Schedule {
        + doctor : List<Doctor>
        + appointments : List<Appointment>
        + updateSchedule()
        + getAvailableTimeSlots()
        + createAppointmentSchedule()
        + addApointmentDoctor()
        + dropAppoimtmentSchedule()
    
    }

    class SystemAdmin {
        + managePatients()
        + updatePatients()
        
    }


    Patient "1" -- "many" MedicalRecord : has
    Patient "1" -- "1" Schedule
    Doctor "1" -- "many" MedicalRecord : has
    Doctor "1" -- "many" Patient : attends
    


    Doctor "1" -- "1" Schedule : has
    Appointment "1" -- "1" Patient : schedules
    Appointment "many" -- "1" Doctor : schedules
    Schedule "1" -- "many" Appointment : includes

    
    SystemAdmin "1" -- "many" Patient : manages 
    SystemAdmin "1" -- "many" Schedule : manages 
    SystemAdmin "1" -- "many" MedicalRecord : manages 

}
@enduml
