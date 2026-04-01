from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CreateGame(BaseModel):
    home_team: str
    away_team: str
    date: datetime
    sport_level: str
    status: str

class GameResponse(CreateGame):
    id: int
    model_config = ConfigDict(from_attributes=True)