import mysql.connector
import json

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
    
    print(f"{'ID':<5} {'MARCA':<15} {'MODELO':<15} {'COLOR':<10} {'KM':<10} {'PRECIO':<10}")
    print("-" * 70)
    
    for coche in cursor.fetchall():
        print(f"{coche[0]:<5} {coche[1]:<15} {coche[2]:<15} {coche[3]:<10} {coche[4]:<10} {coche[5]:<10}")

except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")
    
finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
