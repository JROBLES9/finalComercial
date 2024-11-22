from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
import models, schemas
from sqlalchemy import text

passport_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función auxiliar
def row_to_dict(row):
    return dict(row)

# Consultas ORM para Pasaporte

# Obtener todos los pasaportes (Find)
@passport_router.get("/pasaportes/find/", response_model=List[schemas.Pasaporte])
def find_pasaportes(db: Session = Depends(get_db)):
    pasaportes = db.query(models.Pasaporte).all()
    return pasaportes

# Obtener un pasaporte por ID (FindById)
@passport_router.get("/pasaportes/{pasaporte_id}", response_model=schemas.Pasaporte)
def find_pasaporte_by_id(pasaporte_id: int, db: Session = Depends(get_db)):
    pasaporte = db.query(models.Pasaporte).filter(models.Pasaporte.id == pasaporte_id).first()
    if pasaporte is None:
        raise HTTPException(status_code=404, detail="Pasaporte no encontrado")
    return pasaporte

# Filtrar pasaportes por persona
@passport_router.get("/pasaportes/persona/{persona_id}", response_model=List[schemas.Pasaporte])
def find_pasaportes_by_persona(persona_id: int, db: Session = Depends(get_db)):
    pasaportes = db.query(models.Pasaporte).filter(models.Pasaporte.persona_id == persona_id).all()
    return pasaportes

# Filtrar pasaportes por país
@passport_router.get("/pasaportes/pais/{pais_id}", response_model=List[schemas.Pasaporte])
def find_pasaportes_by_pais(pais_id: int, db: Session = Depends(get_db)):
    pasaportes = db.query(models.Pasaporte).filter(models.Pasaporte.pais_id == pais_id).all()
    return pasaportes

# Filtrar pasaportes por continente
@passport_router.get("/pasaportes/continente/{continente_id}", response_model=List[schemas.Pasaporte])
def find_pasaportes_by_continente(continente_id: int, db: Session = Depends(get_db)):
    pasaportes = db.query(models.Pasaporte).filter(models.Pasaporte.continente_id == continente_id).all()
    return pasaportes

# Consultas en crudo (raw) para Pasaporte

# Obtener todos los pasaportes (Find) - Raw
@passport_router.get("/raw/pasaportes/", response_model=List[schemas.Pasaporte])
def raw_find_pasaportes(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM pasaportes")).fetchall()
    pasaportes = [row_to_dict(row) for row in result]
    return pasaportes

# Obtener un pasaporte por ID (FindById) - Raw
@passport_router.get("/raw/pasaportes/{pasaporte_id}", response_model=schemas.Pasaporte)
def raw_find_pasaporte_by_id(pasaporte_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM pasaportes WHERE id = :id"), {"id": pasaporte_id}
    ).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Pasaporte no encontrado")
    pasaporte = row_to_dict(result)
    return pasaporte

# Filtrar pasaportes por persona - Raw
@passport_router.get("/raw/pasaportes/persona/{persona_id}", response_model=List[schemas.Pasaporte])
def raw_find_pasaportes_by_persona(persona_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM pasaportes WHERE persona_id = :persona_id"), {"persona_id": persona_id}
    ).fetchall()
    pasaportes = [row_to_dict(row) for row in result]
    return pasaportes

# Filtrar pasaportes por país - Raw
@passport_router.get("/raw/pasaportes/pais/{pais_id}", response_model=List[schemas.Pasaporte])
def raw_find_pasaportes_by_pais(pais_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM pasaportes WHERE pais_id = :pais_id"), {"pais_id": pais_id}
    ).fetchall()
    pasaportes = [row_to_dict(row) for row in result]
    return pasaportes

# Filtrar pasaportes por continente - Raw
@passport_router.get("/raw/pasaportes/continente/{continente_id}", response_model=List[schemas.Pasaporte])
def raw_find_pasaportes_by_continente(continente_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM pasaportes WHERE continente_id = :continente_id"), {"continente_id": continente_id}
    ).fetchall()
    pasaportes = [row_to_dict(row) for row in result]
    return pasaportes
