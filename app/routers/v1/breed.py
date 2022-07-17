from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.breed import Breed
from app.config.database import get_db
from app.schemas.breed import RequestBreed
from app.exceptions.breed import *
import copy

router = APIRouter(prefix="/api/v1", tags=["Breed"])


@router.get("/breed/{id}")
async def read_breed(id: int, db: Session = Depends(get_db)):
    """Handle READ operation of breed with id."""
    breeds = db.query(Breed).filter(Breed.id == id).first()

    if breeds is None:
        raise UnExistingBreedException(id)
    return breeds


@router.get("/breeds")
async def read_breeds(page: int, size: int, db: Session = Depends(get_db)):
    """Handle READ operation of all breeds in DB."""
    breeds = db.query(Breed).offset(page).limit(size).all()

    if breeds is None or len(breeds) == 0:
        raise EmptyBreedTable()
    return breeds


@router.post("/breed")
async def create_breed(request_breed: RequestBreed, db: Session = Depends(get_db)):
    """Handle CREATE operation of request_breed."""
    existing_breed = db.query(Breed).filter(Breed.name == request_breed.name).first()

    if existing_breed is not None:
        raise ExistingBreedException(request_breed.name)

    breed = Breed(
        name=request_breed.name,
        size=request_breed.size,
        energy_level=request_breed.energy_level,
        image_link=request_breed.image_link,
    )
    db.add(breed)
    db.flush()
    result = copy.copy(breed)
    db.commit()
    return result


@router.delete("/breed/{id}")
async def delete_breed(id: int, db: Session = Depends(get_db)):
    """Handle DELETE operation of breed with id."""
    existing_breed = db.query(Breed).filter(Breed.id == id).first()

    if existing_breed is None:
        raise UnExistingBreedException(id)

    db.delete(existing_breed)
    db.commit()
    return JSONResponse(
        status_code=200, content={"detail": "Breed has been deleted successfully"}
    )


@router.put("/breed/{id}")
async def update_breed(
    id: int, request_breed: RequestBreed, db: Session = Depends(get_db)
):
    """Handle UPDATE operation of request_breed with id."""
    existing_breed = db.query(Breed).filter(Breed.id == id).first()
    if existing_breed is None:
        raise UnExistingBreedException(id)

    existing_name = db.query(Breed).filter(Breed.name == request_breed.name).first()
    if existing_name is not None and id != existing_name.id:
        raise ExistingBreedException(request_breed.name)

    new_breed = Breed(
        id=id,
        name=request_breed.name,
        size=request_breed.size,
        energy_level=request_breed.energy_level,
        image_link=request_breed.image_link,
    )

    db.delete(existing_breed)
    db.add(new_breed)
    db.flush()
    result = copy.copy(new_breed)
    db.commit()
    return result
