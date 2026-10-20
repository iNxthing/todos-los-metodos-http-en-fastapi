from fastapi import FastAPI
from pydantic import BaseModel
import random
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


@app.get("/luchador/{id}")
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
def actualizar_ganador(id: int, datos: luchador):
    for l in luchadores:
        if l["id"]== id:            
            l["nombre"] = datos.nombre
            l["edad"] = datos.edad
            l["victorias"] = datos.victorias
            l["estaEliminado"] = datos.estaEliminado
            return l





@app.get("/AgregarCombate{id1},{id2}")
def iniciar_combate(id1: int, id2: int):
    idluchador1 = None
    idluchador2 = None

    for luchador in luchadores:
        if id1 == luchador["id"]:
            idluchador1 = luchador["id"]
            if luchador["estaEliminado"] == True:
                return {"Mensaje": f" {luchador["nombre"]} esta eliminado"}
        if id2 == luchador["id"]:
            idluchador2 = luchador["id"]
            if luchador["estaEliminado"] == True:
                return {"Mensaje": f" {luchador["nombre"]} esta eliminado"}

        

    if idluchador1 is None or idluchador2 is None:
        return {"mensaje": "Uno o ambos luchadores no encontrados"}

    if idluchador1 == idluchador2:
        return {"mensaje": "No se puede luchar contra uno mismo"}

    ganador = random.choice([idluchador1, idluchador2])

    
    for l in luchadores:
        if l["id"] == ganador:
            l["victorias"] += 1 
        
    for l in luchadores:
        if l["id"] == idluchador1 or l["id"] == idluchador2:
            if l["id"] != ganador:
                l["estaEliminado"] = True
        
    if(idluchador1 != idluchador2 and idluchador2 != idluchador1):
        if(len(combates) <= 0):
            id = 1
        else:
            id = len(combates) + 1 

        nuevo_combate ={
            "id": id,
            "idluchador1": idluchador1,
            "idluchador2": idluchador2,
            "ganador": ganador,
            "finalizado": True
        }
        combates.append(nuevo_combate)
    else:
        return {
            "mensaje": "No se pudo agregar el combate"
        }

    return {
        "combates": combates
    }



