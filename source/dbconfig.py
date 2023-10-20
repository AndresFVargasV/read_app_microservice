import pyodbc

server = 'localhost'
database = 'crud_microservices'
username = 'sa'
password ='123456789'

def get_connection():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return conn
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)



