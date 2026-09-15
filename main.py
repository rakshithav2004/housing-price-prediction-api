from pyexpat import features
import joblib
import io
import pandas as pd
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

app = FastAPI()
model = joblib.load("california_housing_model.pkl")
feature_names = joblib.load("california_housing_features.pkl")

class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0, description="Median income of Neighborhood")
    HouseAge: float = Field(gt=0, description="Average house age")
    AveRooms: float = Field(gt=0, description="Average number of rooms")
    AveBedrms: float = Field(gt=0, description="Average number of bedrooms")
    Population: float = Field(gt=0, description="Population")
    AveOccup: float = Field(gt=0, description="Average occupancy")
    Latitude: float = Field(ge=32, le=42, description="Latitude")
    Longitude: float = Field(ge=-125, le=-114, description="Longitude")

@app.get("/")
def home():
    return {
        "message": "Welcome to the California Housing Price Prediction API!",
        "endpoints": {
            "POST /predict": "Predict house price based on features"
            },
        "status": "API is running" 
    }    

@app.get("/health")
def health_check():
    return {"status": "API is healthy",
            "model_status": "RandomForestRegressor",
            "features": features,
            "avg_error":"$39,000"
            }

@app.post("/predict")
def predict_price(features: HouseFeatures):
    try:
        input_data = pd.DataFrame([{
            "MedInc": features.MedInc,
            "HouseAge": features.HouseAge,
            "AveRooms": features.AveRooms,
            "AveBedrms": features.AveBedrms,
            "Population": features.Population,
            "AveOccup": features.AveOccup,
            "Latitude": features.Latitude,
            "Longitude": features.Longitude
        }])
        prediction = model.predict(input_data)[0]
        predicted_price= prediction * 100000

        return {"predicted_price": f"${predicted_price:,.0f}",
                "predicted_price_short": f"${prediction:,.2f} hundred thousand",
                "confidence_range":f"${predicted_price - 39000:,.0f} to ${predicted_price + 39000:,.0f}"}
    
    except Exception as e:
        raise HTTPException(status_code=500, 
                            detail="Prediction failed: " + str(e))

@app.post("/predict_csv")
async def predict_price_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
    contents = await file.read()
    df=pd.DataFrame(io.BytesIO(contents))
    required_columns = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise HTTPException(status_code=400, detail=f"Missing required columns: {', '.join(missing_columns)}")

    if len(df)==0:
        raise HTTPException(status_code=400, detail="CSV file is empty.")

    try:
        predictions = model.predict(df[required_columns])
        df['Predicted_column'] = df['Predicted_column'].apply(lambda x: f"${x:,.0f}")
        output = df.to_csv(index=False)

        return StreamingResponse(io.StringIO(output), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=predictions.csv"})

    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction failed: " + str(e))