from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class reporte(BaseModel):
    ubicacion: str
    tipo: str
    personas_afectadas: int
    prioridad: str




reportesList = [
    {
        "id": 1,
        "ubicacion": "Santa Marta - El Rodadero",
        "tipo": "Accidente de transito",
        "personas_afectadas": 5,
        "prioridad": "alta"

    },
    {
        "id": 2,
        "ubicacion": "Santa Marta - Bonda",
        "tipo": "Incendio de Buses",
        "personas_afectadas": 15,
        "prioridad": "alta"

    },
    {
        "id": 3,
        "ubicacion": "Santa Marta - Timayui",
        "tipo": "Corte de fluido electrico",
        "personas_afectadas": 170,
        "prioridad": "bajo"

    }


]

@app.get("/")
def home():
    return {
        "mensaje": "Hola mundo"
    }


@app.get("/ListarReportes")
def mostrar_reportes():
    return {
        "Reportes": reportesList
    }

@app.get("/Reporte{id}")
def reporte_por_id(id: int):
    for r in reportesList:
        if  r["id"] == id:
            return r
        
    raise HTTPException(status_code=404, detail="No se encontro")

@app.get("/Reporten/{prioridad}")
def reporte_por_nivel(prioridad: str):
    reporte_encontrado = []
    for r in reportesList:
        if  r["prioridad"] == prioridad:
            reporte_encontrado.append(r)
    if len(reporte_encontrado) > 0:
        return {
            "Mensaje": "Reportes encontrados",
            "Reportes": reporte_encontrado
        }
        
    raise HTTPException(status_code=404, detail="No se encontro")


@app.post("/Reportar")
def agregar_reporte(datos: reporte):
    nuevo_reporte = {
        "id": len(reportesList) + 1,
        "ubicacion": datos.ubicacion,
        "tipo": datos.tipo,
        "personas_afectadas": datos.personas_afectadas,
        "prioridad": datos.prioridad
    }
    reportesList.append(nuevo_reporte)
    return {
        "Mensaje": "Reporte agregado con exito",
        "Nuevo Reporte": nuevo_reporte 
    }


@app.delete("/BorrarReporte{id}")
def borrar(id: int):
    for r in reportesList:
        if  r["id"] == id:
            reportesList.remove(r)
            return {
                "mensaje": "reporte borrado con exito"
            }
        
    raise HTTPException(status_code=404, detail="No se encontro")

@app.put("/ActualizarReporte{id}")
def actualizar(id: int , datos: reporte):
    for r in reportesList:
        if  r["id"] == id:
            r["ubicacion"] = datos.ubicacion
            r["tipo"] = datos.tipo
            r["personas_afectadas"] = datos.personas_afectadas
            r["prioridad"] = datos.prioridad
            return {
                "Mensaje": "Datos actualizados",
                "Reportes": reportesList
            }



