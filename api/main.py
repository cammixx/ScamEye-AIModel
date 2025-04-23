# api/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from urllib.parse import urlparse
import requests
import pandas as pd
from ml_model import extract_features  # assumes it's importable

app = FastAPI()

# Load trained model (we'll save it later from ml_model.py)
model = joblib.load("malicious_url_model.pkl")

class URLInput(BaseModel):
    url: str

def resolve_url(url: str) -> str:
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.url
    except requests.exceptions.RequestException:
        return url  # fallback to original

@app.post("/predict")
def predict_url(input_data: URLInput):
    final_url = resolve_url(input_data.url)
    features = extract_features(final_url)
    df = pd.DataFrame([features])
    prediction = model.predict_proba(df)[0][1]  # get risk probability (1 = malicious)
    risk_percentage = round(prediction * 100)
    return {"url": final_url, "risk": risk_percentage}
