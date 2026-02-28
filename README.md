# 🏦 Sistema de Predicción de Fuga de Clientes (Bank Churn) - Pipeline MLOps

## 🎯 1. Definición del Problema
La retención de clientes es un pilar crítico en la rentabilidad bancaria. Este proyecto implementa un pipeline de Machine Learning automatizado para predecir el "churn" (fuga) de clientes. El objetivo es identificar usuarios con alta probabilidad de abandono para permitir intervenciones proactivas del equipo de fidelización.

* **Métrica de éxito:** Superar un Accuracy del 85% y mantener un F1-Score equilibrado (debido al desbalance de clases en datos de fuga).

## 📊 2. Dataset y Selección de Variables (Features)
El modelo se alimenta de un dataset transaccional y demográfico. Las variables principales analizadas son:
* **CreditScore:** Puntaje crediticio del cliente.
* **Geography/Gender:** Datos demográficos (procesados mediante One-Hot Encoding).
* **Age:** Identificada como una de las variables con mayor poder predictivo.
* **Balance & EstimatedSalary:** Indicadores de salud financiera del cliente.
* **IsActiveMember:** Variable binaria de comportamiento actual.

## 🧪 3. Experimentación y Preparación de Datos
Durante la fase de análisis exploratorio (EDA) documentada en `notebooks/`, se determinó que:
* **Limpieza:** No se encontraron valores nulos significativos, pero se estandarizaron las escalas de salario y balance.
* **Ingeniería de Características:** Se aplicó `StandardScaler` a las variables numéricas para optimizar la convergencia del algoritmo.
* **Experimentos:** Se compararon modelos de Regresión Logística frente a **Random Forest**, siendo este último el seleccionado por su capacidad de manejar relaciones no lineales.

## ⚙️ 4. Entrenamiento y Modelado
El proceso de entrenamiento se encuentra en `src/train.py`:
* **Algoritmo:** Random Forest Classifier.
* **Validación:** Se utilizó una división de 80/20 para entrenamiento y prueba.
* **Resultados:** * **Accuracy:** 87%
    * **F1-Score:** 0.72 (Demuestra robustez en la detección de la clase minoritaria).

## 🚀 5. Model Serving y Deployment
La solución se expone mediante un microservicio de alta disponibilidad:
* **API:** Desarrollada con **FastAPI**, permitiendo predicciones en tiempo real mediante el endpoint `/predict`.
* **Containerización:** El proyecto incluye un `Dockerfile` que encapsula todas las dependencias, asegurando la portabilidad del modelo entre entornos de desarrollo y producción.

## 📝 6. Conclusiones y Resultados
* **Insights:** Los clientes mayores de 45 años con un balance alto pero baja actividad en productos son el segmento con mayor riesgo de fuga.
* **Limitaciones:** El modelo actual no incluye variables externas (tasas de interés del mercado o competencia) que podrían enriquecer la predicción.
* **Lecciones Aprendidas:** La modularización del código (separar preparación, entrenamiento y serving) fue clave para integrar Docker sin errores de rutas o dependencias.
* **Mejoras Futuras:** Implementar un sistema de monitoreo de *Data Drift* para detectar cuando el modelo necesite un re-entrenamiento debido a cambios en el mercado financiero.

---

### 🛠️ Guía de Ejecución
1.  **Construir la imagen:** `docker build -t churn-api-model .`
2.  **Correr el contenedor:** `docker run -p 8000:8000 churn-api-model`
3.  **Probar:** Acceder a `http://localhost:8000/docs` para interactuar con la interfaz Swagger.