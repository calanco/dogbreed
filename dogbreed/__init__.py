from fastapi import FastAPI
import dogbreed.api.home as home

app = FastAPI()

app.include_router(home.router)
