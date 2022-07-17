from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.database import get_db


def is_database_online(db: Session = Depends(get_db)):
    """Check if a raw SELECT 1 query works without exceptions"""
    try:
        # to check database we will execute raw query
        db.execute("SELECT 1")
        return {"database": "online"}
    except Exception:
        return False
