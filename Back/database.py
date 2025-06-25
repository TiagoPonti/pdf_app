import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv() # Asegúrate de que esta línea esté al principio

# Leemos la URL completa directamente desde las variables de entorno
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

# Una pequeña comprobación para evitar errores
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("La variable de entorno DATABASE_URL no está definida.")

# Si la URL viene de Render, a veces usa 'postgres://' que SQLAlchemy prefiere como 'postgresql://'
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()