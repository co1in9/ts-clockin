from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis
import os

import json

class Request(BaseModel):
    device: str
    position_x: Optional[float]
    position_y: Optional[float]

app = FastAPI()
redis = Redis(host="redis", port=6379, password=os.getenv('REDIS_PASSWORD'))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add")
async def add(request: Request):
    redis.publish('clockin', json.dumps(request.dict()))
    return {"code": 200, "message": "added"}
