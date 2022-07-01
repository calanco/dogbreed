from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.models.breed import Breed
from app.db.database import get_db
import logging

router = APIRouter(prefix='/api/v1', tags=["Breed"])


@router.get("/breed/{id}")
async def read_breed(id: int, db: Session = Depends(get_db)):
    try:
        breeds = db.query(Breed).filter(Breed.id == id).first()
    except Exception:
        logging.error(f"Error while reading breed {id} from DB", exc_info=True)
        raise HTTPException(status_code=500)

    if breeds is None:
        raise HTTPException(status_code=404, detail="No breed has been found")
    return breeds


@router.get("/breeds")
async def read_breeds(db: Session = Depends(get_db)):
    try:
        breeds = db.query(Breed).all()
    except Exception:
        logging.error("Error while reading breeds from DB", exc_info=True)
        raise HTTPException(status_code=500)

    if breeds is None:
        logging.warn("No breed has been found, check DB table")
        raise HTTPException(status_code=404, detail="No breed has been found")
    return breeds
