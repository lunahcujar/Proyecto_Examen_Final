from fastapi import FastAPI

app = FastAPI()

from templates.routes import router
# Incluir las rutas
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
