# =========================================================
# PRODUCTION BACKEND: main.py
# =========================================================

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import uvicorn

# ---------------------------------------------------------
# Import Feature Engineering Function
# ---------------------------------------------------------

from features import create_features

# ---------------------------------------------------------
# FastAPI Setup
# ---------------------------------------------------------

app = FastAPI(
    title="Car Price Estimation API",
    description="ML Backend for predicting used car prices.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Load Pipeline
# ---------------------------------------------------------

try:

    pipeline = joblib.load(
        "production_car_price_pipeline.pkl"
    )

    print(
        "✅ Model loaded successfully!"
    )

except Exception as e:

    pipeline = None

    print(
        f"❌ Failed to load model: {e}"
    )

# ---------------------------------------------------------
# Request Schema
# ---------------------------------------------------------

class CarData(BaseModel):

    brand: str = Field(
        ...,
        json_schema_extra={
            "example": "BMW"
        }
    )

    model: str = Field(
        ...,
        json_schema_extra={
            "example": "X5"
        }
    )

    year: int = Field(
        ...,
        json_schema_extra={
            "example": 2020
        }
    )

    transmission: str = Field(
        ...,
        json_schema_extra={
            "example": "Semi-Auto"
        }
    )

    mileage: float = Field(
        ...,
        json_schema_extra={
            "example": 25000
        }
    )

    fuelType: str = Field(
        ...,
        json_schema_extra={
            "example": "Diesel"
        }
    )

    tax: float = Field(
        ...,
        json_schema_extra={
            "example": 150
        }
    )

    mpg: float = Field(
        ...,
        json_schema_extra={
            "example": 45.2
        }
    )

    engineSize: float = Field(
        ...,
        json_schema_extra={
            "example": 2.0
        }
    )

# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/")
def home():

    return {

        "status": "API is running",

        "model_ready": (
            pipeline is not None
        )

    }

# ---------------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------------

@app.post("/predict")
def predict_price(
    car: CarData
):

    if pipeline is None:

        raise HTTPException(
            status_code=500,
            detail="Model not loaded."
        )

    try:

        df = pd.DataFrame([
            car.model_dump()
        ])

        prediction = pipeline.predict(
            df
        )[0]

        return {

            "success": True,

            "estimated_price_gbp": round(
                float(prediction),
                2
            )

        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

# ---------------------------------------------------------
# Run Server
# ---------------------------------------------------------

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )