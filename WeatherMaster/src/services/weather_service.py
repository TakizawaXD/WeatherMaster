from sqlalchemy.orm import Session
from models.weather import Weather
import requests
import os

class WeatherService:
    def __init__(self, db: Session):
        self.db = db

    def get_current_weather(self, city: str):
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            raise Exception(f"Error fetching weather data: {data.get('message', 'Unknown error')}")
        
        weather = Weather(
            city=data['name'],
            temperature=data['main']['temp'],
            humidity=data['main']['humidity'],
            conditions=data['weather'][0]['description']
        )
        
        self.db.add(weather)
        self.db.commit()
        return weather

    def get_forecast(self, city: str):
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            raise Exception(f"Error fetching forecast data: {data.get('message', 'Unknown error')}")
        
        forecast_data = []
        for item in data['list']:
            forecast_data.append({
                'date': item['dt_txt'],
                'temperature': item['main']['temp'],
                'humidity': item['main']['humidity'],
                'conditions': item['weather'][0]['description']
            })
        
        return forecast_data