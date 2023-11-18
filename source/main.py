from flask import Flask, jsonify, make_response, Response
from bson import json_util
import json
from io import BytesIO
import base64
from PIL import Image
import dbconfig as dbase
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'msg': 'Hello World'})

@app.route('/api/get', methods=['GET'])
def get():
    # Ejemplo de uso
    conexion = dbase.establecer_conexion()

    # Verifica si la conexión fue exitosa
    if conexion:
        # Selecciona la base de datos y la colección
        db, collection = dbase.seleccionar_bd_y_coleccion(conexion, "crud", "crudmicroservices")

        usuarios = collection.find()

        # Lista para almacenar la información de los usuarios con imágenes decodificadas
        usuarios_con_imagenes = []

        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
            usuarios_con_imagenes.append(usuario)

        # Cierra la conexión al finalizar
        dbase.cerrar_conexion(conexion)

        # Devuelve la respuesta JSON después de la iteración
        return Response(json.dumps({'usuarios': usuarios_con_imagenes}, default=json_util.default), mimetype='application/json')
    else:
        return make_response(jsonify({'error': 'No se pudo establecer la conexión con MongoDB'}), 500)

if __name__ == '__main__':
    app.run(debug=True, port=5001)