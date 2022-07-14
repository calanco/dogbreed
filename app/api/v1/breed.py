from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.breed import Breed
from app.database import get_db
from app.schemas.breed import RequestBreed
from app.api.exceptions import ExistingBreedException, UnExistingBreedException
import copy
import logging

router = APIRouter(prefix='/api/v1', tags=["Breed"])


@router.get("/breed/{id}")
async def read_breed(id: int, db: Session = Depends(get_db)):
    """Handle READ operation of breed with id."""
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
    """Handle READ operation of all breeds in DB."""
    try:
        breeds = db.query(Breed).all()
    except Exception:
        logging.error("Error while reading breeds from DB", exc_info=True)
        raise HTTPException(status_code=500)

    if breeds is None:
        logging.warn("No breed has been found, check DB table")
        raise HTTPException(status_code=404, detail="No breed has been found")
    return breeds


@router.post("/breed")
async def create_breed(request_breed: RequestBreed,
                       db: Session = Depends(get_db)):
    """Handle CREATE operation of request_breed."""
    try:
        existing_breed = db.query(Breed) \
            .filter(Breed.name == request_breed.name).first()

        if existing_breed is not None:
            raise ExistingBreedException(request_breed.name)

        breed = Breed(
            name=request_breed.name,
            size=request_breed.size,
            energy_level=request_breed.energy_level,
            image_link=request_breed.image_link
        )
        db.add(breed)
        db.flush()
        result = copy.copy(breed)
        db.commit()
        return result
    except ExistingBreedException as e:
        logging.warn(e.detail)
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception:
        logging.error("Error while creating breed into DB", exc_info=True)
        raise HTTPException(status_code=500)


@router.delete("/breed/{id}")
async def delete_breed(id: int, db: Session = Depends(get_db)):
    """Handle DELETE operation of breed with id."""
    try:
        existing_breed = db.query(Breed).filter(Breed.id == id).first()

        if existing_breed is None:
            raise UnExistingBreedException(id)

        db.delete(existing_breed)
        db.commit()
    except UnExistingBreedException as u:
        raise HTTPException(status_code=u.status_code, detail=u.detail)
    except Exception:
        logging.error("Error while deleting breed from DB", exc_info=True)
        raise HTTPException(status_code=500)


@router.put("/breed/{id}")
async def update_breed(id: int, request_breed: RequestBreed,
                       db: Session = Depends(get_db)):
    """Handle UPDATE operation of request_breed with id."""
    try:
        existing_breed = db.query(Breed).filter(Breed.id == id).first()
        if existing_breed is None:
            raise UnExistingBreedException(id)

        existing_name = db.query(Breed) \
            .filter(Breed.name == request_breed.name).first()
        if existing_name is not None and id != existing_name.id:
            raise ExistingBreedException(request_breed.name)

        new_breed = Breed(
            id=id,
            name=request_breed.name,
            size=request_breed.size,
            energy_level=request_breed.energy_level,
            image_link=request_breed.image_link
        )

        db.delete(existing_breed)
        db.add(new_breed)
        db.flush()
        result = copy.copy(new_breed)
        db.commit()
        return result
    except (UnExistingBreedException, ExistingBreedException) as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception:
        logging.error("Error while deleting breed from DB", exc_info=True)
        raise HTTPException(status_code=500)
