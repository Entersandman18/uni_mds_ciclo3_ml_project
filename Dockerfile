# 1. Usar una imagen de Python ligera
FROM python:3.12-slim

# 2. Establecer la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requisitos e instalar librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código y el modelo al contenedor
COPY src/ ./src/
COPY models/ ./models/
COPY data/ ./data/

# 5. Exponer el puerto donde corre la API
EXPOSE 8000

# 6. Comando para iniciar la API al encender el contenedor
CMD ["uvicorn", "src.serving:app", "--host", "0.0.0.0", "--port", "8000"]