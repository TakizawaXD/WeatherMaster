from fastapi import FastAPI
from src.db.database import init_db
from src.api.routes import router as weather_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(weather_router)

@app.get("/")
async def root():
    return {"message": "Welcome to WeatherMaster API"}