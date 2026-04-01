from fastapi import FastAPI
from database import engine, Base
from routers import games

app = FastAPI()
app.include_router(games.router, prefix="/api")
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ok"}