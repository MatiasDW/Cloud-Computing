# Imagen base optimizada para FastAPI
FROM tiangolo/uvicorn-gunicorn:python3.10 AS carlemany-backend-base

# Actualizar pip
RUN pip install --upgrade pip

# Copiar e instalar dependencias
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Establecer el directorio de trabajo
WORKDIR /carlemany-backend

# Copiar el código del proyecto
COPY . .

# Comando para iniciar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "error"]
