from fastapi import FastAPI
import mysql.connector

# Definir la conexión a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="zoopoli"
)
# Crear una instancia de FastAPI
app = FastAPI()

# Definir la ruta para la consulta
@app.get("/consultar_animalicos")
async def consultar_animalicos():
    consulta = "SELECT * FROM animal;"
    
    # Ejecutar la consulta
    cursor = conexion.cursor()
    cursor.execute(consulta)
    
    # Obtener los resultados de la consulta
    animalicos = cursor.fetchall()
    
    # Imprimir los resultados en la terminal
    for animalico in animalicos:
        print(animalico)
    
    # Cerrar el cursor
    cursor.close()
    
    # Retornar una respuesta
    return {"mensaje": "Consulta realizada exitosamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
