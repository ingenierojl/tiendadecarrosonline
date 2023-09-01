from multiprocessing import connection
from fastapi import *
from fastapi.templating import *
from fastapi.staticfiles import StaticFiles
import mysql.connector
import uvicorn
from funcion_conexion import *
from funcion_insertar import *
templates = Jinja2Templates(directory="D:/ServidorWeb/static")
app=APIRouter() #crear una instancia de fastapi
#configurar la instancia de fastapi con el directorio
app.mount("/static", StaticFiles(directory="D:\ServidorWeb\static"),name="static")

@app.get("/")#RUTA O ENDPOINT
async def home(request: Request):
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/registrar")
def form_post(request: Request, fn: str = Form(...), ap: str = Form(...), em: str = Form(...), pas: str = Form(...)):
    print(fn)
    print(ap)
    print(em)
    print(pas)
    print("esta es la ruta registrar")
    insertar_variables_registro(fn,ap,em,pas)
    return templates.TemplateResponse("/index.html",{"request":request})    
    

if __name__=='__main__':
    print("Método principal aqui inicia la ejecución")
    uvicorn.run(app, host="localhost", port=8081)


