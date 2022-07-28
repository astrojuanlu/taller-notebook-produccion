import datetime as dt

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello, world!"}


@app.get("/train_and_persist")
async def train_and_persist():
    return {"success": True}


@app.get("/predict")
async def predict(
    dteday: dt.date,
    weathersit: str,
    temp: float,
    atemp: float,
    hum: float,
    windspeed: float,
):
    return {"success": True}
