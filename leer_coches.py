import mysql.connector
import json
from prettytable import PrettyTable

# Leer credenciales desde el JSON
with open('config.json', 'r') as f:
    config = json.load(f)

try:
    conexion = mysql.connector.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
    
    cursor = conexion.cursor()
    cursor.execute("SELECT id, marca, modelo, color, km, precio FROM coches")
    
    # Crear la tabla y definir las columnas
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"]
    
    # Añadir cada fila a la tabla
    for coche in cursor.fetchall():
        tabla.add_row(coche)
    
    # Imprimir la tabla
    print(tabla)

except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")
    
finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
