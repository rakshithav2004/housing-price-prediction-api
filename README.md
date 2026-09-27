🏠 Housing Price Prediction API

A machine learning-powered Housing Price Prediction REST API built with FastAPI and Scikit-learn.

The application provides two prediction modes:

- 🏠 Single House Prediction — enter house details and receive a predicted price.
- 📁 CSV Batch Prediction — upload a CSV containing multiple houses, generate predictions for all rows, and download the resulting CSV file with predicted prices.

The machine learning model is trained using the California Housing dataset and a Random Forest Regression algorithm.

---

🚀 Features

- 🧠 Machine learning-based housing price prediction
- 🌲 Random Forest Regression model
- ⚡ FastAPI REST API
- 📄 Interactive Swagger API documentation
- 🏠 Single-house price prediction
- 📁 CSV file upload
- 📊 Batch prediction for multiple houses
- ⬇️ Download prediction results as a CSV file
- ✅ Request validation using Pydantic
- 🔍 CSV column validation
- 💾 Trained model saved using Joblib
- 🐍 Python backend
- 🔄 Reproducible model training

---

🛠️ Tech Stack

Technology| Purpose
Python| Programming language
FastAPI| REST API framework
Uvicorn| ASGI server
Scikit-learn| Machine learning
Pandas| Data processing
NumPy| Numerical operations
Pydantic| Request validation
Joblib| Model serialization

---

📊 Dataset

This project uses the California Housing dataset provided by Scikit-learn.

The dataset contains 20,640 records and 8 input features.

Features

Feature| Description
"MedInc"| Median income
"HouseAge"| Median house age
"AveRooms"| Average number of rooms
"AveBedrms"| Average number of bedrooms
"Population"| Block population
"AveOccup"| Average house occupancy
"Latitude"| Geographic latitude
"Longitude"| Geographic longitude

Target

Price

The target values are represented in units of $100,000.

For example:

4.0 = $400,000

---

📂 Project Structure

housing-price-prediction-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
│
├── models/
│   └── house_price_model.pkl
│
├── train.py
├── requirements.txt
├── .gitignore
└── README.md

---

⚙️ Installation

1. Clone the Repository

git clone https://github.com/rakshithav2004/housing-price-prediction-api.git

Navigate into the project:

cd housing-price-prediction-api

---

2. Create a Virtual Environment

Windows

py -m venv venv

Activate the environment:

.\venv\Scripts\Activate.ps1

If PowerShell blocks script execution:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then:

.\venv\Scripts\Activate.ps1

---

3. Install Dependencies

pip install -r requirements.txt

---

🧠 Train the Machine Learning Model

The model can be trained using:

python train.py

The training process performs the following steps:

Load California Housing Dataset
          ↓
Explore Dataset
          ↓
Check Missing Values
          ↓
Separate Features and Target
          ↓
Train/Test Split
          ↓
Train Random Forest Model
          ↓
Generate Predictions
          ↓
Evaluate Model
          ↓
Save Trained Model

The trained model is saved as:

models/house_price_model.pkl

---

📈 Model Evaluation

The model is evaluated using three metrics:

MAE

Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

RMSE

Root Mean Squared Error

Measures prediction error while giving greater weight to larger errors.

R² Score

Coefficient of Determination

Measures how well the model explains the variation in the target values.

The training script prints these metrics after training.

Example:

Model Evaluation
----------------
MAE  : 0.32
RMSE : 0.50
R2   : 0.81

«Actual values may vary depending on model configuration and training changes.»

---

▶️ Run the FastAPI Application

Start the API using:

uvicorn app.main:app --reload

The application will run at:

http://127.0.0.1:8000

---

📚 API Documentation

FastAPI automatically generates interactive API documentation.

Open:

http://127.0.0.1:8000/docs

You can test the API directly using Swagger UI.

Alternative documentation:

http://127.0.0.1:8000/redoc

---

🏠 Single House Prediction

The API allows users to provide the details of one house and receive a predicted price.

Input

Example request:

{
  "MedInc": 8.32,
  "HouseAge": 41.0,
  "AveRooms": 6.98,
  "AveBedrms": 1.02,
  "Population": 322.0,
  "AveOccup": 2.55,
  "Latitude": 37.88,
  "Longitude": -122.23
}

Prediction

The trained Random Forest model processes the input and returns the predicted housing price.

Example:

{
  "predicted_price": 4.25
}

Since the target is expressed in units of $100,000:

4.25 = $425,000

---

📁 CSV Batch Prediction

The API also supports batch prediction using CSV files.

Instead of sending one house at a time, users can upload a CSV containing multiple housing records.

Example Input CSV

MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude
8.32,41,6.98,1.02,322,2.55,37.88,-122.23
7.25,52,7.25,1.01,240,2.10,37.85,-122.25
3.85,30,5.50,1.05,500,3.20,37.75,-122.20

---

🔄 CSV Prediction Flow

User uploads CSV
       ↓
Validate file
       ↓
Validate required columns
       ↓
Read CSV using Pandas
       ↓
Load trained ML model
       ↓
Generate predictions
       ↓
Add predicted_price column
       ↓
Create output CSV
       ↓
User downloads result

---

⬇️ Download Prediction Results

After processing the uploaded CSV, the API generates a new CSV file containing the original input features along with the predicted price.

Example output:

MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude,predicted_price
8.32,41,6.98,1.02,322,2.55,37.88,-122.23,4.25
7.25,52,7.25,1.01,240,2.10,37.85,-122.25,3.87
3.85,30,5.50,1.05,500,3.20,37.75,-122.20,2.91

The generated file can be downloaded directly by the user.

This makes the API useful for processing larger batches of housing records and saving the prediction results for further analysis.

---

🔍 CSV Validation

The CSV upload endpoint validates that the required model features are present.

Required columns:

MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude

If required columns are missing or the uploaded file is invalid, the API returns an appropriate validation error instead of attempting a prediction.

---

🧪 Testing

The API can be tested using:

- Swagger UI
- Postman
- cURL
- Any REST API client

Swagger:

http://127.0.0.1:8000/docs

---

🏗️ Architecture

                         ┌─────────────────┐
                         │   User / Client │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     FastAPI     │
                         │      API        │
                         └────────┬────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
             Single Prediction            CSV Upload
                    │                           │
                    │                    Pandas Processing
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Trained Random  │
                         │ Forest Model    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    Prediction   │
                         └────────┬────────┘
                                  │
                         ┌────────┴────────┐
                         │                 │
                         ▼                 ▼
                    JSON Response    Download CSV

---

📌 API Capabilities

Capability| Supported
Single prediction| ✅
CSV upload| ✅
Batch prediction| ✅
Download predictions| ✅
Request validation| ✅
CSV validation| ✅
Swagger documentation| ✅
Machine learning model| ✅
Model persistence| ✅

---

🔮 Future Improvements

Possible future improvements include:

- Docker containerization
- Automated unit and integration tests
- CI/CD with GitHub Actions
- Authentication and authorization
- Prediction history
- Database integration
- Model versioning
- Model performance monitoring
- Cloud deployment
- Frontend interface for easier CSV uploads
- Support for multiple ML models
- Automated model retraining

---

👩‍💻 Author

Rakshitha V

GitHub:

"https://github.com/rakshithav2004"

---

⭐ Project

If you find this project useful, feel free to ⭐ star the repository.a 
