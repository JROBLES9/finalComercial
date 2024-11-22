from fastapi import FastAPI
from database import engine, Base
from routers import passport_router
import uvicorn

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(passport_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
