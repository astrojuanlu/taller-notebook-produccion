import datetime as dt

from fastapi import FastAPI

from bikesmodel import train_and_persist, predict

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello, world!"}


# Beware! Exposing train_and_persist
# allows anyone to run the training


@app.post("/train_and_persist")
async def do_train_and_persist():
    train_and_persist()
    return {"success": True}


@app.get("/predict")
async def do_predict(
    dteday: dt.date,
    hr: int,
    weathersit: str,
    temp: float,
    atemp: float,
    hum: float,
    windspeed: float,
):
    result = predict(
        dteday.isoformat(),
        hr,
        weathersit,
        temp,
        atemp,
        hum,
        windspeed,
    )
    return {"number_cyclists": result}
