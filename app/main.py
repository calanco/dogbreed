from fastapi import FastAPI
import app.api.routes.home as home

app = FastAPI()

app.include_router(home.router)
