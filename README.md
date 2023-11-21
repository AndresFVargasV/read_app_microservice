# Microservicio de CRUD con Flask

Esta aplicación es una API construida con Flask que proporciona operaciones la opción de leer de un CRUD (Crear, Leer, Actualizar, Eliminar) para usuarios almacenados en una base de datos MongoDB. Está API es creada bajo la arquitectura de microservicios. La API permite a los usuarios realizar las siguientes acciones:

Obtener Saludo: Acceder a un mensaje de saludo básico desde la ruta /api.

Leer Usuarios: Leer todos los usuario almacenados en la BD mediante una solicitud GET a la ruta /api/get/.

Leer Usuario: Leer un usuario específico mediante una solicitud GET a la ruta /api/get/{numero_documento}.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/AndresFVargasV/read_app_microservices.git
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Asegúrate de tener MongoDB instalado y configurado.

2. Configura la conexión a la base de datos en `dbconfig.py`.

## Uso

1. Inicia la aplicación:

    ```bash
    python nombre-de-tu-app.py
    ```

2. Abre tu navegador y visita [http://localhost:5001/api](http://localhost:5001/api) para obtener un saludo básico.

3. Para obtener todos los usuarios registrados:

    ```http
    GET http://localhost:5001/api/get
    ```

4. Para obtener un usuario específico por su número de documento:

    ```http
    GET http://localhost:5001/api/get/numero-de-documento
    ```

    Reemplaza `numero-de-documento` con el número de documento del usuario que deseas obtener.

## Endpoints

- **GET /api**: Devuelve un mensaje simple de "Hello World".
- **GET /api/get**: Obtiene todos los usuarios registrados.
- **GET /api/get/{numero_documento}**: Obtiene un usuario específico por su número de documento.

## Contribuciones

Si encuentras algún problema o tienes alguna mejora, siéntete libre de abrir un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [Apache License](LICENSE) para obtener más detalles.

