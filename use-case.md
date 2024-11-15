@startuml use_case_diagram
left to right direction

actor Patient
actor Doctor
actor Register
actor SystemAdmin

rectangle "Clinic Information System" {
    usecase "Make Appointment" as MA
    usecase "Record Visit" as RV
    usecase "Manage Medical Records" as MMR
    usecase "Get Medical History " as GMH
    usecase "Manage User Accounts" as MUA
    usecase "Register Patient in System " as RPS
    usecase "Remove Patient from System" as RPR
}

Patient -- MA
Patient -- MMR
Patient -- RPS
Patient -- RPR
Patient -- GMH
Doctor -- RV
Doctor -- GMH
Register -- MA
Register -- RV
Register -- RPS
Register -- MMR
SystemAdmin -- MUA
SystemAdmin -- RPR
SystemAdmin -- MA
SystemAdmin -- RV
SystemAdmin -- MMR
SystemAdmin -- GMH
SystemAdmin -- RPS

@enduml

