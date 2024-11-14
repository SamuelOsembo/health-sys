# main.py
from models import register_patient, book_appointment, cancel_appointment, check_in_patient, record_prescription

def main():
    print("Welcome to the Health Centre Management System")
    while True:
        print("\nSelect an option:")
        print("1. Register Patient")
        print("2. Book Appointment")
        print("3. Cancel Appointment")
        print("4. Check-in Patient")
        print("5. Record Prescription")
        print("0. Exit")

        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            address = input("Enter address: ")
            patient_number = input("Enter patient number: ")
            register_patient(name, dob, address, patient_number)
        
        elif choice == '2':
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            book_appointment(patient_id, doctor_id, date, time)
        
        elif choice == '3':
            appointment_id = int(input("Enter appointment ID to cancel: "))
            cancel_appointment(appointment_id)
        
        elif choice == '4':
            patient_id = int(input("Enter patient ID for check-in: "))
            check_in_patient(patient_id)
        
        elif choice == '5':
            appointment_id = int(input("Enter appointment ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            patient_id = int(input("Enter patient ID: "))
            medication = input("Enter medication name: ")
            dosage = input("Enter dosage: ")
            record_prescription(appointment_id, doctor_id, patient_id, medication, dosage)
        
        elif choice == '0':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
