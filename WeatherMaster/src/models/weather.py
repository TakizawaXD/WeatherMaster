from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    conditions = Column(String(100))
    feels_like = Column(Float)  # Sensación térmica
    timestamp = Column(String(50))  # Para almacenar la fecha y hora de la consulta

    def __repr__(self):
        return f"<Weather(city={self.city}, temperature={self.temperature}, conditions={self.conditions})>"