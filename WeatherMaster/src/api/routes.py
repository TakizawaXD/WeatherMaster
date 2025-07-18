from fastapi import APIRouter, HTTPException
from typing import List
from src.models.weather import WeatherResponse, WeatherForecast
from src.services.weather_service import get_current_weather, get_weather_forecast

router = APIRouter()

@router.get("/weather/current", response_model=WeatherResponse)
async def read_current_weather(city: str):
    weather = await get_current_weather(city)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return weather

@router.get("/weather/forecast", response_model=List[WeatherForecast])
async def read_weather_forecast(city: str):
    forecast = await get_weather_forecast(city)
    if not forecast:
        raise HTTPException(status_code=404, detail="Forecast data not found")
    return forecast