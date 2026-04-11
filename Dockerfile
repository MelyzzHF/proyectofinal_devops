# Usamos una sola etapa para asegurar que no se pierdan rutas
FROM python:3.11-slim

WORKDIR /app

# Instalamos dependencias directamente
COPY requirements.txt .
RUN pip install --no-cache-dir flask gunicorn boto3

# Copiamos el código
COPY app.py .

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando directos
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
