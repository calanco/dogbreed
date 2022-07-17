from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_health import health
from app.routers.health import is_database_online
import app.routers.home as home
import app.routers.v1.breed as breed
from app.exceptions import (
    ExistingBreedException,
    UnExistingBreedException,
    EmptyBreedTable,
)
import logging

app = FastAPI()

app.add_api_route("/health", health([is_database_online]))

app.include_router(home.router)
app.include_router(breed.router)


@app.exception_handler(ExistingBreedException)
def existing_breed_exception_handler(request: Request, exc: ExistingBreedException):
    return JSONResponse(status_code=409, content={"detail": exc.detail})


@app.exception_handler(UnExistingBreedException)
def unexisting_breed_exception_handler(request: Request, exc: UnExistingBreedException):
    return JSONResponse(status_code=404, content={"detail": exc.detail})


@app.exception_handler(EmptyBreedTable)
def empty_breed_table_exception_handler(request: Request, exc: EmptyBreedTable):
    logging.warn("Breed table is empty, please check DB")
    return JSONResponse(status_code=404, content={"detail": exc.detail})
