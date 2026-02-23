from fastapi import FastAPI
from carbon_check import get_carbon_intensity, is_carbon_high

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sustainability DevOps API Running"}

@app.get("/carbon")
def carbon():
    intensity = get_carbon_intensity()
    return {"carbon_intensity": intensity}

@app.get("/status")
def status():
    high = is_carbon_high()
    return {
        "carbon_high": high,
        "message": "Pause build" if high else "Safe to proceed"
    }
