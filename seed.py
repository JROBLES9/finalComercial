from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Crear las tablas en la base de datos si no existen
models.Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()
    try:
        # Verificar si ya hay datos para evitar duplicados
        if db.query(models.Continente).first():
            print("Los datos de semilla ya han sido insertados.")
            return

        # Crear continentes
        continente1 = models.Continente(nombre="América")
        continente2 = models.Continente(nombre="Europa")
        continente3 = models.Continente(nombre="Asia")
        db.add_all([continente1, continente2, continente3])
        db.commit()
        db.refresh(continente1)
        db.refresh(continente2)
        db.refresh(continente3)

        # Crear países
        pais1 = models.Pais(nombre="México", continente_id=continente1.id)
        pais2 = models.Pais(nombre="España", continente_id=continente2.id)
        pais3 = models.Pais(nombre="Japón", continente_id=continente3.id)
        db.add_all([pais1, pais2, pais3])
        db.commit()
        db.refresh(pais1)
        db.refresh(pais2)
        db.refresh(pais3)

        # Crear personas
        persona1 = models.Persona(nombre="Juan Pérez", pais_id=pais1.id)
        persona2 = models.Persona(nombre="María García", pais_id=pais2.id)
        persona3 = models.Persona(nombre="Taro Yamada", pais_id=pais3.id)
        db.add_all([persona1, persona2, persona3])
        db.commit()
        db.refresh(persona1)
        db.refresh(persona2)
        db.refresh(persona3)

        # Crear pasaportes
        pasaporte1 = models.Pasaporte(
            numero="MX123456",
            persona_id=persona1.id,
            pais_id=pais1.id,
            continente_id=continente1.id
        )
        pasaporte2 = models.Pasaporte(
            numero="ES654321",
            persona_id=persona2.id,
            pais_id=pais2.id,
            continente_id=continente2.id
        )
        pasaporte3 = models.Pasaporte(
            numero="JP987654",
            persona_id=persona3.id,
            pais_id=pais3.id,
            continente_id=continente3.id
        )
        db.add_all([pasaporte1, pasaporte2, pasaporte3])
        db.commit()

        print("Datos de semilla insertados correctamente.")
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error al insertar los datos de semilla: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
