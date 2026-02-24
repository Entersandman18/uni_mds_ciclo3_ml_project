import pandas as pd
import os
from sklearn.model_selection import train_test_split

def prepare_data():
    # 1. Rutas de archivos (usando la estructura de tu repo)
    raw_data_path = "data/raw/bank_churn.csv"
    output_folder = "data/training"
    
    if not os.path.exists(raw_data_path):
        print(f"❌ Error: No se encontró el archivo en {raw_data_path}")
        return

    # 2. Cargar datos
    df = pd.read_csv(raw_data_path)
    print("✅ Datos cargados correctamente.")

    # 3. Limpieza (Sección D: Transformaciones)
    # Eliminamos columnas que no aportan (ID, Apellido, etc.)
    cols_to_drop = ['RowNumber', 'CustomerId', 'Surname']
    df_cleaned = df.drop(columns=cols_to_drop)

    # 4. Ingeniería de características (Encoding para variables de texto)
    # Convertimos 'Geography' y 'Gender' en números que el modelo entienda
    df_cleaned = pd.get_dummies(df_cleaned, columns=['Geography', 'Gender'], drop_first=True)

    # 5. División de datos (Entrenamiento y Prueba)
    train_df, test_df = train_test_split(df_cleaned, test_size=0.2, random_state=42)

    # 6. Guardar resultados (Requisito de la Sección D)
    os.makedirs(output_folder, exist_ok=True)
    train_df.to_csv(f"{output_folder}/train_cleaned.csv", index=False)
    test_df.to_csv(f"{output_folder}/test_cleaned.csv", index=False)
    
    print(f"🎯 ¡Éxito! Dataset listo en: {output_folder}/train_cleaned.csv")

if __name__ == "__main__":
    prepare_data()