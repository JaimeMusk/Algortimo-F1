# Utiliza una imagen de Python 3.8 (o la versión que prefieras)
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de código y el modelo
COPY . .

# Actualizar pip y luego instalar las dependencias específicas
RUN pip install --upgrade pip && \
    pip install --no-cache-dir pandas==1.5.3 gradio scikit-learn


# Exponer el puerto en el que Gradio correrá
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Ejecutar la aplicación
CMD ["python", "new_app.py"]
