from flask import Flask, request, jsonify
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
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)