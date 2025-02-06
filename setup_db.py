import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('legalbuddy.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for storing user responses
cursor.execute('''
    CREATE TABLE responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        practice_area TEXT NOT NULL,
        represented TEXT NOT NULL,
        incident_date TEXT,
        incident_location TEXT,
        is_ongoing TEXT,
        case_details TEXT,
        phone TEXT,
        email TEXT,
        address TEXT,
        birthday TEXT,
        contact_consent TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
