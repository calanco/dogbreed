from fastapi import FastAPI
import app.api.home as home
import app.api.v1.breed as breed

app = FastAPI()

app.include_router(home.router)
app.include_router(breed.router)
