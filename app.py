from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('legalbuddy.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/responses', methods=['POST'])
def add_response():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO responses (name, practice_area, represented, incident_date, incident_location, is_ongoing, case_details, phone, email, address, birthday, contact_consent)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['practice_area'], data['represented'], data['incident_date'], data['incident_location'], data['is_ongoing'], data['case_details'], data['phone'], data['email'], data['address'], data['birthday'], data['contact_consent']))
    
    conn.commit()
    conn.close()
    return jsonify({'message': 'Response added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
