# 🏠 Housing Price Prediction API

A machine learning-powered REST API built with **FastAPI** that predicts California housing prices using a **Random Forest Regression** model.

The API supports both **individual house price prediction** and **CSV file upload for batch predictions**.

## 🚀 Features

* 🧠 Machine learning-based housing price prediction
* 🌲 Random Forest Regression model
* ⚡ FastAPI REST API
* 📄 Interactive Swagger API documentation
* 🏠 Predict price for a single house
* 📁 Upload CSV files for batch predictions
* 📊 Returns predicted prices for multiple houses
* ✅ Request validation using Pydantic
* 💾 Trained model saved using Joblib
* 🐍 Python-based backend

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Pydantic
* Joblib
* Uvicorn

## 📂 Project Structure

```text
housing-price-prediction-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── model.py
│
├── models/
│   └── house_price_model.pkl
│
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset

This project uses the **California Housing dataset** provided by Scikit-learn.

The dataset contains the following features:

| Feature    | Description                |
| ---------- | -------------------------- |
| MedInc     | Median income              |
| HouseAge   | Median house age           |
| AveRooms   | Average number of rooms    |
| AveBedrms  | Average number of bedrooms |
| Population | Block population           |
| AveOccup   | Average house occupancy    |
| Latitude   | Geographic latitude        |
| Longitude  | Geographic longitude       |

The target variable is:

```text
Price
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/rakshithav2004/housing-price-prediction-api.git
cd housing-price-prediction-api
```

### 2. Create a virtual environment

Windows:

```powershell
py -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🧠 Train the Model

Run:

```bash
python train.py
```

The training script:

1. Loads the California Housing dataset
2. Explores the dataset
3. Splits the data into training and testing sets
4. Trains a Random Forest Regression model
5. Evaluates the model using MAE, RMSE, and R²
6. Saves the trained model

The trained model is saved as:

```text
models/house_price_model.pkl
```

## ▶️ Run the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the prediction endpoints directly from Swagger UI.

## 🏠 Single House Prediction

Send the house features to the prediction endpoint.

Example request:

```json
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
```

Example response:

```json
{
  "predicted_price": 4.25
}
```

> The target values in the California Housing dataset are expressed in units of $100,000.

## 📁 CSV Batch Prediction

The API also supports uploading a CSV file containing multiple houses.

Example CSV:

```csv
MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude
8.32,41,6.98,1.02,322,2.55,37.88,-122.23
7.25,52,7.25,1.01,240,2.10,37.85,-122.25
3.85,30,5.50,1.05,500,3.20,37.75,-122.20
```

The API processes the rows and returns predicted prices for each house.

This makes the API useful for **batch prediction** rather than requiring one API request per house.

## 🔄 Application Flow

```text
                 ┌──────────────────┐
                 │   Client/User    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    FastAPI       │
                 │      API         │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
      Single Prediction        CSV Upload
              │                       │
              ▼                       ▼
        Input Validation       Pandas Processing
              │                       │
              └───────────┬───────────┘
                          ▼
                 ┌──────────────────┐
                 │ Trained Random   │
                 │ Forest Model     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Predicted Price  │
                 └──────────────────┘
```

## 📈 Model Evaluation

The model is evaluated using:

* **MAE** — Mean Absolute Error
* **RMSE** — Root Mean Squared Error
* **R² Score** — Coefficient of Determination

These metrics help measure how accurately the model predicts housing prices.

## 🔮 Future Improvements

* Add authentication and authorization
* Add model versioning
* Add prediction history
* Add Docker support
* Add automated tests
* Add CI/CD pipeline
* Add model performance monitoring
* Deploy the API to a cloud platform

## 👩‍💻 Author

**Rakshitha Bai V**

GitHub: `rakshithav2004`

---

⭐ If you found this project useful, consider giving it a star!
