# models.py
from database import get_connection

def register_patient(name, dob, address, patient_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, date_of_birth, address, patient_number) VALUES (?, ?, ?, ?)",
                   (name, dob, address, patient_number))
    conn.commit()
    conn.close()
    print(f"Patient {name} registered successfully.")

def book_appointment(patient_id, doctor_id, date, time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (patient_id, doctor_id, date, time, status) VALUES (?, ?, ?, ?, ?)",
                   (patient_id, doctor_id, date, time, 'Booked'))
    conn.commit()
    conn.close()
    print(f"Appointment booked successfully for Patient ID {patient_id} with Doctor ID {doctor_id}.")

def cancel_appointment(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE appointments SET status = 'Canceled' WHERE id = ?", (appointment_id,))
    conn.commit()
    conn.close()
    print(f"Appointment ID {appointment_id} canceled successfully.")

def check_in_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE appointments SET status = 'Checked-in' WHERE patient_id = ? AND status = 'Booked'", (patient_id,))
    conn.commit()
    conn.close()
    print(f"Patient ID {patient_id} checked in successfully.")

def record_prescription(appointment_id, doctor_id, patient_id, medication, dosage):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prescriptions (appointment_id, doctor_id, patient_id, medication, dosage) VALUES (?, ?, ?, ?, ?)",
                   (appointment_id, doctor_id, patient_id, medication, dosage))
    conn.commit()
    conn.close()
    print(f"Prescription recorded for Appointment ID {appointment_id}.")
