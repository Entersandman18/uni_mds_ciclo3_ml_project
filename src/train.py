import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def train_model():
    # 1. Cargar los datos limpios que generamos ayer
    train_path = "data/training/train_cleaned.csv"
    test_path = "data/training/test_cleaned.csv"
    
    if not os.path.exists(train_path):
        print(f"❌ Error: No se encontró {train_path}. ¿Corriste data_preparation.py?")
        return

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    # 2. Separar características (X) y objetivo (y)
    # 'Exited' es la columna que queremos predecir (1 si se fue, 0 si se quedó)
    X_train = train_df.drop('Exited', axis=1)
    y_train = train_df['Exited']
    X_test = test_df.drop('Exited', axis=1)
    y_test = test_df['Exited']

    # 3. Configurar y entrenar el modelo (Sección D del proyecto)
    print("⏳ Entrenando el modelo Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4. Evaluación rápida
    predictions = model.predict(X_test)
    print("\n📊 Reporte de Clasificación:")
    print(classification_report(y_test, predictions))
    print(f"✅ Precisión total (Accuracy): {accuracy_score(y_test, predictions):.2f}")

    # 5. Guardar el modelo (Requisito para el despliegue/Serving)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/bank_churn_model.pkl")
    print("\n🎯 Modelo guardado exitosamente en 'models/bank_churn_model.pkl'")

if __name__ == "__main__":
    train_model()