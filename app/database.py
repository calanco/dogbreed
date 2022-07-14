from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


DB_HOSTNAME = os.environ['DB_HOSTNAME']

SQLALCHEMY_DATABASE_URI = f"postgresql://docker:docker@{DB_HOSTNAME}/dogbreed"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
