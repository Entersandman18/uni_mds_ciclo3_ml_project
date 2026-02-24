from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# 1. Cargar el "cerebro" del modelo que guardaste ayer
model = joblib.load("models/bank_churn_model.pkl")

app = FastAPI(title="API de Auditoría de Fuga de Clientes")

# 2. Definir qué datos necesita recibir la API
class Cliente(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Geography_Germany: int
    Geography_Spain: int
    Gender_Male: int

@app.get("/")
def inicio():
    return {"mensaje": "Sistema de Predicción de Fuga Activo"}

@app.post("/predict")
def predecir(datos: Cliente):
    # Convertir los datos recibidos a un formato que el modelo entienda
    df = pd.DataFrame([datos.dict()])
    
    # Realizar la predicción
    prediccion = model.predict(df)[0]
    probabilidad = model.predict_proba(df)[0][1]
    
    return {
        "se_va": int(prediccion),
        "probabilidad_fuga": f"{probabilidad:.2%}",
        "analisis": "Alto riesgo de fuga" if prediccion == 1 else "Cliente estable"
    }