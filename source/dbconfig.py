from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def establecer_conexion():
    try:
        # Intenta establecer la conexión con el servidor MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Verifica si la conexión fue exitosa lanzando una excepción si no lo fue
        client.admin.command('ismaster')

        print("Conexión establecida exitosamente")
        return client

    except ConnectionFailure:
        # Captura la excepción ConnectionFailure en caso de fallo de conexión
        print("Error al establecer la conexión a MongoDB")
        return None

def seleccionar_bd_y_coleccion(client, db_name, collection_name):
    if client:
        # Selecciona la base de datos y la colección
        db = client[db_name]
        collection = db[collection_name]
        return db, collection
    else:
        return None, None

def cerrar_conexion(client):
    if client:
        # Cierra la conexión solo si se estableció correctamente
        client.close()
        print("Conexión cerrada")




