import uuid

from fastapi import APIRouter, Request, Form, Depends, HTTPException, UploadFile, File, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse, FileResponse
from users import User


router = APIRouter()
templates = Jinja2Templates(directory="templates")
# Página principal
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})





#usuario
@router.get("/registro", response_class=HTMLResponse)
def mostrar_formulario_registro(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

from conexion_db import get_db, SessionLocal

@router.post("/api/usuarios")
def registrar_usuario(
    name: str = Form(...),
    mail: str = Form(...),
    photo: UploadFile = File(None),
    db: SessionLocal = Depends(get_db)
):

        nuevo_usuario = User(
            name=name, mail=mail, image_url=photo
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

        return {
            "mensaje": "✅ Usuario registrado correctamente",
            "id": nuevo_usuario.id,
            "image_url": nuevo_usuario.image_url
        }

