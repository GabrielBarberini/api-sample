# api.py

from typing import Optional
from rocketpy import Environment, Flight
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
from rocket_simulation import Calisto

class Env(BaseModel, Environment):
    railLength: Optional[float] = 5.2
    latitude: float 
    longitude: float
    elevation: Optional[int] = 1400
    date: Optional[datetime.datetime] = datetime.datetime.today() + datetime.timedelta(days=1) 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "RocketPy Sample API"}

# Environment
@app.post("/env/")
async def create_env(env: Env):
    #Env.setAtmosphericModel(type='StandardAtmosphere', file='GFS')
    env_dict = env.dict()
    #TestFlight = Flight(rocket=Calisto, environment=Env, inclination=85, heading=0)
    #TestFlight.info()
    #TestFlight.allInfo()
    return env_dict 
