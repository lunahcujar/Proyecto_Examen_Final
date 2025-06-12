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