from flask import Flask, request, jsonify
import json
from datetime import date
import base64 
import dbconfig as db



app = Flask(__name__) 

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'msg': 'Hello World'})

@app.route('/api/get', methods=['GET'])
def get():
    conn = db.get_connection()
    if conn == None:
        return jsonify({'msg': 'No se pudo conectar a la base de datos'})
    cursor = conn.cursor() 
    cursor.execute('SELECT * FROM Personas')
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    results = []
    
    for row in data:
        result_row = {}
        for i, value in enumerate(row):
            if isinstance(value, date):
                result_row[column_names[i]] = value.strftime('%Y-%m-%d')
            elif isinstance(value, bytes): 
                result_row[column_names[i]] = base64.b64encode(value).decode() 
            else:
                result_row[column_names[i]] = value
        results.append(result_row)

    json_data = json.dumps(results)
    cursor.close()
    conn.close()
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)