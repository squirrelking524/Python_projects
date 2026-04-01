from fastapi import APIRouter
import statsapi

router = APIRouter()

@router.get("/games")
def get_games():
    return statsapi.schedule(date='today')