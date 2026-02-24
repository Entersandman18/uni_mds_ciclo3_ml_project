# Proyecto Final MLOps - Predicción de Fuga de Clientes (Bank Churn)

## A) Definición del Problema
Este proyecto implementa un sistema de Machine Learning para predecir la fuga de clientes (churn) en una institución financiera. El objetivo es identificar clientes con alta probabilidad de abandonar el banco para tomar acciones preventivas.
* **Métrica de éxito:** Lograr un Accuracy superior al 80%.

## B) Estructura del Proyecto
El proyecto sigue una estructura modular:
* `data/`: Datasets crudos y procesados.
* `models/`: Modelos serializados (.pkl).
* `notebooks/`: Evidencia de experimentación y EDA.
* `src/`: Código fuente (Preparación, Entrenamiento y Serving).

## C) Experimentación (EDA)
Se realizó un análisis exploratorio en `notebooks/eda_experimentation.ipynb`, identificando que variables como la edad, el balance y el número de productos son críticas para la predicción.

## D) Desarrollo y Entrenamiento
* **Preparación:** `src/data_preparation.py` realiza la limpieza y encoding.
* **Entrenamiento:** `src/train.py` utiliza un algoritmo de **Random Forest**.
* **Resultado:** Se obtuvo una precisión (Accuracy) del **87%**.

## E) Model Serving (API)
Se implementó una API con **FastAPI** en `src/serving.py`.
* **Prueba:** La API fue validada mediante la interfaz Swagger en `/docs`.

## F) Containerización (Docker)
El proyecto cuenta con un `Dockerfile` para asegurar la portabilidad.
* **Construcción:** `docker build -t churn-api-image .`
* **Ejecución:** `docker run -p 8000:8000 churn-api-image`

