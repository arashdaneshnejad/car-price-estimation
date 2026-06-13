# =========================================================
# PRODUCTION BACKEND: main.py
# =========================================================

import os
import json
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
# Load Metadata (NEW)
# ---------------------------------------------------------

METADATA_PATH = "car_metadata.json"
car_metadata = {}

try:
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            car_metadata = json.load(f)
        print("✅ Metadata loaded successfully!")
    else:
        print("⚠️ Metadata file not found! Make sure 'car_metadata.json' is in the same directory.")
except Exception as e:
    print(f"❌ Failed to load metadata: {e}")

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
        ),
        
        "metadata_ready": (
            len(car_metadata) > 0
        )

    }

# ---------------------------------------------------------
# Metadata Endpoints for Frontend (NEW)
# ---------------------------------------------------------

@app.get("/brands")
def get_brands():
    """Returns a list of all available car brands."""
    if not car_metadata:
        raise HTTPException(status_code=500, detail="Metadata not loaded.")
    return {"brands": list(car_metadata.keys())}


@app.get("/models/{brand}")
def get_models(brand: str):
    """Returns a list of models for a specific brand."""
    if brand not in car_metadata:
        raise HTTPException(status_code=404, detail="Brand not found.")
    return {"models": list(car_metadata[brand].keys())}


@app.get("/details/{brand}/{model}")
def get_model_details(brand: str, model: str):
    """Returns available transmissions, fuel types, and engine sizes for a specific car."""
    if brand not in car_metadata:
        raise HTTPException(status_code=404, detail="Brand not found.")
    
    # Handling potential trailing/leading spaces in model names that might exist in the dataset
    model_keys = list(car_metadata[brand].keys())
    matched_model = next((m for m in model_keys if m.strip() == model.strip()), None)

    if not matched_model:
        raise HTTPException(status_code=404, detail="Model not found for this brand.")
    
    return car_metadata[brand][matched_model]


@app.get("/all-metadata")
def get_all_metadata():
    """Returns the entire tree structure for frontend caching."""
    if not car_metadata:
        raise HTTPException(status_code=500, detail="Metadata not loaded.")
    return car_metadata

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
