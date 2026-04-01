from database import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, DateTime

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String, nullable=False, index=True)
    away_team = Column(String, nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True)
    sport_level = Column(String, index=True)
    status = Column(String, index=True)
    home_team_score = Column(Integer, default=0, index=True)
    away_team_score = Column(Integer, default=0, index=True)
    home_team_hits = Column(Integer, default=0)
    away_team_hits = Column(Integer, default=0)