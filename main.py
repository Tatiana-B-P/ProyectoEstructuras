from fastapi import FastAPI
import logica as lg

# Crear una instancia de FastAPI
app = FastAPI()

# Ruta de inicio
@app.get("/api/v1/search")
async def read_root():
    return lg.buscador()

# Ruta con parámetros
@app.get("/api/v1/search/{item_id}")
async def read_item(item_id: str):
    #intenta ejecutar el codigo a continuacion. De tener un error como el que la palabra pasada por parametro en la URL no sea un indice permitido para busqueda, de ser asi ejecutara la excepcion.
    try:
        #Genera un diccionario en el que la llave es el item por el que se agruparon las tutelas
        return {item_id:lg.buscador()[item_id]}
    except Exception:
        return "Palabra no encontrada"