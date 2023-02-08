from fastapi import FastAPI, Body
from typing import Union, Optional
from pydantic import BaseModel

class LightBulb:
    def __init__(self, room_id : int, mode: int, status: int, intensity: int):
        self.room_id = room_id
        self.mode = mode
        self.status = status
        self.intensity = intensity

all_light_bulb = []
for i in range(3):
    temp = LightBulb(i,0,0,100)
    all_light_bulb.append(temp)

        

app = FastAPI()

@app.get("/")
def get_status():
    return {"room_id": 0, "status": 0, "mode": 0, "inden": 100}

@app.put("/")
def turn_light_button(room_id: int, status: Union[int, None] = None):
    return {"room_id": 0, "status": 0, "mode": 0, "inden": 100}

@app.put("/")
def turn_light_sensor(room_id: int, status: Union[int, None] = None):
    return {"item_id": "order"}

@app.put("/")
def change_mode(room_id: int, mode: int):
    return {"item_id": "order"}

@app.put("/")
def change_intensity(room_id: int, intensity):
    return {"item_id": "order"}
