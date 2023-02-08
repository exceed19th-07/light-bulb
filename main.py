from fastapi import FastAPI, Body
from typing import Union, Optional
from pydantic import BaseModel

class LightBulb:
    def __init__(self, room_id : int, mode: int, status: bool, intensity: int):
        self.room_id = room_id
        self.mode = mode # 0 = manual, 1 = auto
        self.status = status # 0 = off, 1 = on
        self.intensity = intensity

all_light_bulb = []
for i in range(3):
    temp = LightBulb(i,0,False,100)
    all_light_bulb.append(temp)


app = FastAPI()

@app.get("/")
def get_status():
    all = []
    for i in all_light_bulb:
        all.append({"room_id": i.room_id, "mode": i.mode, "status": i.status, "intensity": i.intensity})
    return {"result": all}

@app.put("/turn_light_button")
def turn_light_button(room_id: int, status: Union[bool, None] = None):
    if all_light_bulb[room_id].mode == 1: # auto mode cant manually use to button
        return {"room_id": all_light_bulb[room_id].room_id, "status": all_light_bulb[room_id].status, "mode": all_light_bulb[room_id].mode, "inden": all_light_bulb[room_id].intensity}
    if status is None:
        if all_light_bulb[room_id].status == False:
            all_light_bulb[room_id].status = True
        else:
            all_light_bulb[room_id].status = False
    else:
        all_light_bulb[room_id].status = status
    return {"room_id": all_light_bulb[room_id].room_id, "status": all_light_bulb[room_id].status, "mode": all_light_bulb[room_id].mode, "inden": all_light_bulb[room_id].intensity}

@app.put("/turn_light_sensor")
def turn_light_sensor(room_id: int, status: Union[bool, None] = None):
    if status is None:
        if all_light_bulb[room_id].status == False:
            all_light_bulb[room_id].status = True
        else:
            all_light_bulb[room_id].status = False
    else:
        all_light_bulb[room_id].status = status
    return {"room_id": all_light_bulb[room_id].room_id, "status": all_light_bulb[room_id].status, "mode": all_light_bulb[room_id].mode, "inden": all_light_bulb[room_id].intensity}

@app.put("/change_mode")
def change_mode(room_id: int, mode: Union[int, None] = None):
    if mode is None:
        if all_light_bulb[room_id].mode == 0:
            all_light_bulb[room_id].mode = 1
        else:
            all_light_bulb[room_id].mode = 0
    else:
        all_light_bulb[room_id].mode = mode
    return {"room_id": all_light_bulb[room_id].room_id, "status": all_light_bulb[room_id].status, "mode": all_light_bulb[room_id].mode, "inden": all_light_bulb[room_id].intensity}

@app.put("/change_intensity")
def change_intensity(room_id: int, intensity: int):
    all_light_bulb[room_id].intensity = intensity
    return {"room_id": all_light_bulb[room_id].room_id, "status": all_light_bulb[room_id].status, "mode": all_light_bulb[room_id].mode, "inden": all_light_bulb[room_id].intensity}
