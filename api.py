# api.py

from typing import Optional
from rocketpy import Environment, Flight
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
from rocket_simulation import Calisto
from templates import flight_summary 

class Env(BaseModel):
    railLength: Optional[float] = 5.2
    latitude: float 
    longitude: float
    elevation: Optional[int] = 1400
    date: Optional[datetime.datetime] = datetime.datetime.today() + datetime.timedelta(days=1) 

app = FastAPI()

# Environment
@app.post("/env/")
async def create_env(env: Env):
    env = Environment(
            railLength=env.railLength,
            latitude=env.latitude,
            longitude=env.longitude,
            elevation=env.elevation,
            date=env.date
    )
    env.setAtmosphericModel(type='StandardAtmosphere', file='GFS')
    TestFlight = Flight(rocket=Calisto, environment=env, inclination=85, heading=0)
    summary = flight_summary(TestFlight) 
    return summary
