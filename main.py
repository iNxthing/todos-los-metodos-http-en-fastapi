from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

luchadores = [
    {
        "id": 1,
        "nombre": "Goku",
        "edad": 24,
        "victorias": 0,
        "estaEliminado": False
    },
    {
        "id": 2,
        "nombre": "Vegueta",
        "edad": 32,
        "victorias": 0,
        "estaEliminado": False
    },
    {
        "id": 3,
        "nombre": "Piccolo",
        "edad": 42,
        "victorias": 0,
        "estaEliminado": False
    }


]

combates = []

class luchador(BaseModel):
    nombre: str
    edad: int
    victorias: int
    estaEliminado: bool

class combate(BaseModel):
    luchadorid1: int
    luchadorid2: int
    ganadorid: int
    finalizado: bool

@app.get("/")
def home():
    return {"Mensaje": "Hola Mundo"}

@app.get("/Luchadores")
def mostrar_lucahdores():
    return {"Luchadores": luchadores}


@app.get("/luchador{id}")
def mostrar_porid(id: int):

    for l in luchadores:
        if(l["id"] == id):
            return l



@app.post("/AgregarLuchador")
def agregar_luchador(datos: luchador):
    nuevo_luchador = {
        "id": len(luchadores) + 1,
        "nombre": datos.nombre,
        "edad": datos.edad,
        "victorias": datos.victorias,
        "estaEliminado": datos.estaEliminado

    }
    luchadores.append(nuevo_luchador)

    return {
        "Mensaje": "Luchador agregado con exito",
        "respuesta": nuevo_luchador
    }

@app.delete("/EliminarLuchador{id}")
def eliminar_Luchador(id: int):
    for l in luchadores:
        if(l["id"] == id):
            luchadores.pop(id - 1)
    
    return {
        "Mensaje": "Luchador eliminado "
    }

@app.put("/ActaulizarLucahdor{id}")
def actualizar_ganador(id: int,datos:luchador):
    for l in luchadores:
        if l["id"]== id:            
            l["nombre"] = datos.nombre
            l["edad"] = datos.edad
            l["victorias"] = datos.victorias
            l["estaEliminado"] = datos.estaEliminado
            return l


