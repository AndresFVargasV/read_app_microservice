from flask import Flask, jsonify, make_response, Response
from bson import json_util
import json
from io import BytesIO
import base64
from PIL import Image
import dbconfig as dbase
from flask_cors import CORS

# Inicializa la aplicación Flask
app = Flask(__name__)

# Permite el acceso desde cualquier origen a la API
CORS(app)

# Ruta base para la API
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'msg': 'Hello World'})

# Ruta para obtener todos los usuarios registrados en la base de datos
@app.route('/api/get', methods=['GET'])
def get():
    conexion = dbase.establecer_conexion()

    # Verifica si la conexión fue exitosa
    if conexion:
        
        # Selecciona la base de datos y la colección
        db, collection = dbase.seleccionar_bd_y_coleccion(conexion, "crud", "crudmicroservices")

        # Busca todos los usuarios en la colección
        usuarios = collection.find()

        # Lista para almacenar la información de los usuarios con imágenes decodificadas
        usuarios_id_string = []

        # Iteramos cada usuario para convertir el id de mongodb a string
        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
            usuarios_id_string.append(usuario)

        # Cierra la conexión al finalizar
        dbase.cerrar_conexion(conexion)

        # Devuelve la respuesta JSON después de la iteración
        return Response(json.dumps({'usuarios': usuarios_id_string}, default=json_util.default), mimetype='application/json')
    else:

        # Devuelve la respuesta JSON teniendo en cuenta que la conexión no fue exitosa
        return make_response(jsonify({'error': 'No se pudo establecer la conexión con MongoDB'}), 500)
    
# Ruta para obtener un usuario específico por su número de documento
@app.route('/api/get/<id>', methods=['GET'])
def get_one(id):
    # Establece la conexión con la base de datos
    conexion = dbase.establecer_conexion()

    # Verifica si la conexión fue exitosa
    if conexion:

        # Selecciona la base de datos y la colección
        db, collection = dbase.seleccionar_bd_y_coleccion(conexion, "crud", "crudmicroservices")

        # Busca el usuario por su número de documento
        usuario = collection.find_one({'numero_documento': id})

        # Verifica si el usuario existe
        if usuario:
            # Tomamos el id del usuario dado por mongodb y lo convertimos a string para poder serializarlo
            usuario['_id'] = str(usuario['_id'])

            # Cierra la conexión al finalizar
            dbase.cerrar_conexion(conexion)

            # Devuelve la respuesta JSON
            return Response(json.dumps({'usuario': usuario}, default=json_util.default), mimetype='application/json')
        else:
            # Cierra la conexión al finalizar
            dbase.cerrar_conexion(conexion)

            # Devuelve la respuesta JSON teniendo en cuenta que el usuario no existe
            return make_response(jsonify({'error': 'No se encontró el usuario con el número de documento especificado'}), 404)
    else:
        return make_response(jsonify({'error': 'No se pudo establecer la conexión con MongoDB'}), 500)


# Inicializa la aplicación Flask desde este modeulo base
if __name__ == '__main__':
    app.run(debug=True, port=5001)