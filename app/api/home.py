from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(tags=["Home"])


@router.get("/", response_class=PlainTextResponse)
async def home():
    return "Welcome to Dogbreed!"
