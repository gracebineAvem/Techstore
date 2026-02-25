
# database.py
# Connexion à la base de données pour Techstore By Michelle
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from dotenv import load_dotenv

load_dotenv()


# Forcer SQLite même en ligne si DATABASE_URL n'est pas défini
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
	DATABASE_URL = "sqlite:///./techstore.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
