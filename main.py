from fastapi import FastAPI
from database import engine, Base
from routers import passport_router

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(passport_router)
