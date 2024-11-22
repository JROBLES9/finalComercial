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

# Función auxiliar para convertir filas en diccionarios
def row_to_dict(row):
    return dict(row)

# -------------------------------
# Rutas ORM para Persona
# -------------------------------

# Obtener todas las personas (Find)
@passport_router.get("/personas/find/", response_model=List[schemas.Persona])
def find_personas(db: Session = Depends(get_db)):
    personas = db.query(models.Persona).all()
    return personas

# Obtener una persona por ID (FindById)
@passport_router.get("/personas/{persona_id}", response_model=schemas.Persona)
def find_persona_by_id(persona_id: int, db: Session = Depends(get_db)):
    persona = db.query(models.Persona).filter(models.Persona.id == persona_id).first()
    if persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return persona

# -------------------------------
# Rutas ORM para País
# -------------------------------

# Obtener todos los países (Find)
@passport_router.get("/paises/find/", response_model=List[schemas.Pais])
def find_paises(db: Session = Depends(get_db)):
    paises = db.query(models.Pais).all()
    return paises

# Obtener un país por ID (FindById)
@passport_router.get("/paises/{pais_id}", response_model=schemas.Pais)
def find_pais_by_id(pais_id: int, db: Session = Depends(get_db)):
    pais = db.query(models.Pais).filter(models.Pais.id == pais_id).first()
    if pais is None:
        raise HTTPException(status_code=404, detail="País no encontrado")
    return pais

# -------------------------------
# Rutas ORM para Continente
# -------------------------------

# Obtener todos los continentes (Find)
@passport_router.get("/continentes/find/", response_model=List[schemas.Continente])
def find_continentes(db: Session = Depends(get_db)):
    continentes = db.query(models.Continente).all()
    return continentes

# Obtener un continente por ID (FindById)
@passport_router.get("/continentes/{continente_id}", response_model=schemas.Continente)
def find_continente_by_id(continente_id: int, db: Session = Depends(get_db)):
    continente = db.query(models.Continente).filter(models.Continente.id == continente_id).first()
    if continente is None:
        raise HTTPException(status_code=404, detail="Continente no encontrado")
    return continente

# -------------------------------
# Rutas ORM para Pasaporte
# -------------------------------

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

# -------------------------------
# Rutas RAW para Persona
# -------------------------------

# Obtener todas las personas (Find) - Raw
@passport_router.get("/raw/personas/", response_model=List[schemas.Persona])
def raw_find_personas(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM personas")).fetchall()
    personas = [row_to_dict(row) for row in result]
    return personas

# Obtener una persona por ID (FindById) - Raw
@passport_router.get("/raw/personas/{persona_id}", response_model=schemas.Persona)
def raw_find_persona_by_id(persona_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM personas WHERE id = :id"), {"id": persona_id}
    ).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    persona = row_to_dict(result)
    return persona

# -------------------------------
# Rutas RAW para País
# -------------------------------

# Obtener todos los países (Find) - Raw
@passport_router.get("/raw/paises/", response_model=List[schemas.Pais])
def raw_find_paises(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM paises")).fetchall()
    paises = [row_to_dict(row) for row in result]
    return paises

# Obtener un país por ID (FindById) - Raw
@passport_router.get("/raw/paises/{pais_id}", response_model=schemas.Pais)
def raw_find_pais_by_id(pais_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM paises WHERE id = :id"), {"id": pais_id}
    ).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="País no encontrado")
    pais = row_to_dict(result)
    return pais

# -------------------------------
# Rutas RAW para Continente
# -------------------------------

# Obtener todos los continentes (Find) - Raw
@passport_router.get("/raw/continentes/", response_model=List[schemas.Continente])
def raw_find_continentes(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM continentes")).fetchall()
    continentes = [row_to_dict(row) for row in result]
    return continentes

# Obtener un continente por ID (FindById) - Raw
@passport_router.get("/raw/continentes/{continente_id}", response_model=schemas.Continente)
def raw_find_continente_by_id(continente_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM continentes WHERE id = :id"), {"id": continente_id}
    ).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Continente no encontrado")
    continente = row_to_dict(result)
    return continente

# -------------------------------
# Rutas RAW para Pasaporte
# -------------------------------

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

