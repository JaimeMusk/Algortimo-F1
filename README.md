F1 Final Position Predictor
Proyecto desarrollado por Jaime Ortueta en el contexto de Data Science.

Este proyecto tiene como objetivo predecir la posición final de un piloto en la temporada de Fórmula 1 de 2024. Utiliza técnicas avanzadas de Machine Learning, desde la definición del problema hasta el despliegue en Docker con Gradio, proporcionando una herramienta interactiva y predictiva para el análisis de rendimiento en Fórmula 1.

Descripción del Proyecto
La idea central de este proyecto fue construir un modelo que pueda predecir la posición final de un piloto en el campeonato basado en datos históricos de rendimiento. Después de evaluar varios algoritmos y optimizar sus hiperparámetros, se seleccionó Random Forest Regressor como el modelo final debido a su rendimiento superior.

Estructura del Proyecto
Este repositorio está organizado de la siguiente manera:

notebooks/: Contiene los Jupyter Notebooks utilizados para la exploración de datos, pruebas y experimentos con diferentes modelos.
data/: Archivos de datos (CSV, Parquet, SQLite, etc.) empleados en el procesamiento y entrenamiento del modelo.
app/: Archivos necesarios para el despliegue de la aplicación.
new_app.py: Código principal de la aplicación, que utiliza Gradio para la interfaz de usuario.
Dockerfile: Configuración para crear el entorno de despliegue en Docker.
models/: Archivos de modelos entrenados y otros recursos de Machine Learning.
modelo_entrenado.pkl: Modelo final en formato pickle para su uso en la aplicación.
README.md: Documentación del proyecto con información detallada sobre los archivos y su propósito.
Instalación
Para ejecutar este proyecto en tu máquina local, sigue los siguientes pasos:

Clonar el repositorio:

bash
Copy code
git clone https://github.com/JaimeMusk/F1Prediction.git
cd F1Prediction
Construir la imagen de Docker (opcional, solo si deseas ejecutarlo en un contenedor):

bash
Copy code
docker build -t f1-predictor .
Ejecutar la aplicación:

Para lanzar la aplicación localmente:

bash
Copy code
python3 app/new_app.py
O si prefieres ejecutarla en Docker:

bash
Copy code
docker run -p 7860:7860 f1-predictor
Uso de la Aplicación
La aplicación está diseñada para proporcionar predicciones basadas en el nombre del piloto seleccionado. Los datos de entrada, como los puntos, la posición promedio y la cantidad de DNF (Did Not Finish), se utilizan para calcular una predicción de la posición final en la temporada.

Interfaz de Usuario: La aplicación está construida con Gradio, ofreciendo una interfaz fácil de usar donde puedes seleccionar un piloto y obtener una predicción inmediata de su posición final.
Contribuciones
Las contribuciones son bienvenidas. Para contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama para tu funcionalidad:
bash
Copy code
git checkout -b nueva-funcionalidad
Realiza los commits de tus cambios:
bash
Copy code
git commit -m 'Añadir nueva funcionalidad'
Haz push a la rama:
bash
Copy code
git push origin nueva-funcionalidad
Abre un Pull Request en GitHub.
¡Gracias por tu interés en F1 Final Position Predictor!

Saludos al Mejor profesor del Mundo Hernan :)






