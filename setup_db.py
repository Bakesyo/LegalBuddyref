import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('lawsuitbuddy.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for storing user responses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        practice_area TEXT NOT NULL,
        represented TEXT NOT NULL,
        incident_date TEXT NOT NULL,
        incident_location TEXT NOT NULL,
        is_ongoing TEXT NOT NULL,
        case_details TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        birthday TEXT NOT NULL,
        contact_consent TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
