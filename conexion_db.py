import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

CLEVER_HOST = os.getenv("DB_HOST")
CLEVER_PORT = os.getenv("DB_PORT")
CLEVER_DATABASE = os.getenv("DB_NAME")
CLEVER_USER = os.getenv("DB_USER")
CLEVER_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    pool_size=3,
    max_overflow=2,
    pool_timeout=30,
    pool_pre_ping=True,
    pool_recycle=1800
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()