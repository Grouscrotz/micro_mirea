from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    from settings import settings
    engine = create_engine(settings.postgres_url)
    print("Database engine created")
except Exception as e:
    print(f"Warning: Could not create database engine: {e}")
    engine = None

SessionLocal = sessionmaker(bind=engine) if engine else None
Base = declarative_base()

def get_db():
    if SessionLocal is None:
        raise Exception("Database not configured")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()