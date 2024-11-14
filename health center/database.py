# database.py
import sqlite3

def create_tables():
    connection = sqlite3.connect("health_center.db")
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        date_of_birth TEXT,
                        address TEXT,
                        patient_number TEXT UNIQUE
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY,
                        patient_id INTEGER,
                        doctor_id INTEGER,
                        date TEXT,
                        time TEXT,
                        status TEXT,
                        FOREIGN KEY (patient_id) REFERENCES patients (id),
                        FOREIGN KEY (doctor_id) REFERENCES doctors (id)
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS prescriptions (
                        id INTEGER PRIMARY KEY,
                        appointment_id INTEGER,
                        doctor_id INTEGER,
                        patient_id INTEGER,
                        medication TEXT,
                        dosage TEXT,
                        FOREIGN KEY (appointment_id) REFERENCES appointments (id),
                        FOREIGN KEY (doctor_id) REFERENCES doctors (id),
                        FOREIGN KEY (patient_id) REFERENCES patients (id)
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS receptionists (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                      )''')

    connection.commit()
    connection.close()

def get_connection():
    return sqlite3.connect("health_center.db")
