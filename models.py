from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Continente(Base):
    __tablename__ = 'continentes'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    paises = relationship("Pais", back_populates="continente")
    pasaportes = relationship("Pasaporte", back_populates="continente")

class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    continente_id = Column(Integer, ForeignKey('continentes.id'))
    continente = relationship("Continente", back_populates="paises")
    personas = relationship("Persona", back_populates="pais")
    pasaportes = relationship("Pasaporte", back_populates="pais")

class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    pais_id = Column(Integer, ForeignKey('paises.id'))
    pais = relationship("Pais", back_populates="personas")
    pasaportes = relationship("Pasaporte", back_populates="persona")

class Pasaporte(Base):
    __tablename__ = 'pasaportes'
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, index=True)
    persona_id = Column(Integer, ForeignKey('personas.id'))
    pais_id = Column(Integer, ForeignKey('paises.id'))
    continente_id = Column(Integer, ForeignKey('continentes.id'))
    persona = relationship("Persona", back_populates="pasaportes")
    pais = relationship("Pais", back_populates="pasaportes")
    continente = relationship("Continente", back_populates="pasaportes")
