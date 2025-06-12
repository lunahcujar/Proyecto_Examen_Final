import uuid

from fastapi import APIRouter, Request, Form, Depends, HTTPException, UploadFile, File, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse, FileResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")
# Página principal
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})





#usuario
@router.get("/registro", response_class=HTMLResponse)
async def mostrar_formulario_registro(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

from conexion_db import get_db, SessionLocal

@router.post("/api/usuarios")
async def registrar_usuario(
    name: str = Form(...),
    mail: str = Form(...),
    photo: UploadFile = File(None),
    db: SessionLocal = Depends(get_db)
):
    try:
        image_url = None
        if photo:
            filename = f"{uuid.uuid4()}_{photo.filename}"
            content = await photo.read()
            response = supabase.storage.from_(SUPABASE_BUCKET).upload(filename, content)
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="❌ Error al subir imagen a Supabase")
            image_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{filename}"

        nuevo_usuario = User(
            name=name, mail=mail, type_skin=type_skin, preferences=preferences, image_url=image_url
        )
        db.add(nuevo_usuario)
        await db.commit()
        await db.refresh(nuevo_usuario)

        return {
            "mensaje": "✅ Usuario registrado correctamente",
            "id": nuevo_usuario.id,
            "image_url": nuevo_usuario.image_url
        }

    except Exception as e:
        await db.rollback()
        print("❌ ERROR REGISTRANDO USUARIO EN CLEVER:", repr(e))
        raise HTTPException(status_code=500, detail="Error al registrar usuario")