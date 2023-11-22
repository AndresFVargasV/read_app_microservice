from datetime import datetime

# Función para obtener la fecha formateada
def obtener_fecha_formateada():
    meses_abreviados = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    fecha_actual = datetime.now()

    dia = fecha_actual.day
    mes_abreviado = meses_abreviados[fecha_actual.month - 1]  # Restamos 1 para obtener el índice correcto en la lista
    anio = fecha_actual.year

    # Agrega un cero al día si es menor que 10
    dia_formateado = f'0{dia}' if dia < 10 else f'{dia}'

    # Construye la cadena de formato
    fecha_formateada = f'{dia_formateado}-{mes_abreviado}-{anio}'

    return fecha_formateada

# Función para generar información de log
def info_log(tipo_documento, numero_documento):
    log = {
        'tipo': 'READ',
        'tipo_documento': tipo_documento,
        'numero_documento': numero_documento,
        'fecha': obtener_fecha_formateada(),
        'descripcion': f'Se obtuvo información del usuario: {numero_documento}'
    }

    return log
