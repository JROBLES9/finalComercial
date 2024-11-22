from pydantic import BaseModel

class ContinenteBase(BaseModel):
    nombre: str

class ContinenteCreate(ContinenteBase):
    pass

class Continente(ContinenteBase):
    id: int
    class Config:
        orm_mode = True

class PaisBase(BaseModel):
    nombre: str
    continente_id: int

class PaisCreate(PaisBase):
    pass

class Pais(PaisBase):
    id: int
    class Config:
        orm_mode = True

class PersonaBase(BaseModel):
    nombre: str
    pais_id: int

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: int
    class Config:
        orm_mode = True

class PasaporteBase(BaseModel):
    numero: str
    persona_id: int
    pais_id: int
    continente_id: int

class PasaporteCreate(PasaporteBase):
    pass

class Pasaporte(PasaporteBase):
    id: int
    class Config:
        orm_mode = True
