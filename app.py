from flask import Flask, request, jsonify
import sqlite3
from geopy.geocoders import Nominatim
from news_scraper import get_relevant_cases

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('lawsuitbuddy.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/responses', methods=['POST'])
def add_response():
    data = request.get_json()
    # Validate required fields
    required_fields = ['name', 'practice_area', 'represented', 'incident_date', 'incident_location', 
                       'is_ongoing', 'case_details', 'phone', 'email', 'address', 'birthday', 'contact_consent']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO responses (name, practice_area, represented, incident_date, incident_location, is_ongoing, case_details, phone, email, address, birthday, contact_consent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['name'], data['practice_area'], data['represented'], data['incident_date'],
              data['incident_location'], data['is_ongoing'], data['case_details'], data['phone'],
              data['email'], data['address'], data['birthday'], data['contact_consent']))
        conn.commit()
    except Exception as e:
        conn.rollback()
        app.logger.error("Error while adding response: %s", e)
        return jsonify({'error': 'An error occurred while processing your request.'}), 500
    finally:
        conn.close()
    
    return jsonify({'message': 'Response added successfully!'}), 201

@app.route('/api/cases', methods=['POST'])
def get_local_cases():
    data = request.get_json()
    geolocator = Nominatim(user_agent="lawsuit_buddy")
    
    try:
        location = geolocator.reverse(f"{data['lat']}, {data['lng']}")
        state = location.raw['address'].get('state')
        cases = get_relevant_cases(state)
        
        return jsonify({
            'cases': cases,
            'location': state
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
