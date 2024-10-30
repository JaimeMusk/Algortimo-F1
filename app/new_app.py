import pickle
import gradio as gr
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Cargar el modelo y los datos de los pilotos desde el archivo .pkl
with open("models/modelo_entrenado.pkl", "rb") as file:
    modelo, pilotos_data = pickle.load(file)  # Cargamos tanto el modelo como el DataFrame con los datos de los pilotos

# Extraer los nombres de los pilotos para el menú desplegable
pilot_names = pilotos_data["driver"].tolist()  # Asume que "driver" es la columna con los nombres de los pilotos

# Definir la función de predicción
def predict_final_position(pilot_name):
    # Filtrar los datos del piloto seleccionado
    pilot_data = pilotos_data[pilotos_data["driver"] == pilot_name]
    
    # Extraer las características necesarias como un DataFrame de una fila
    input_data = pilot_data[["points", "average_position", "dnf_count"]]
    
    # Usar el modelo para predecir
    prediction = modelo.predict(input_data)
    return round(prediction[0])

# Crear la interfaz de Gradio
interface = gr.Interface(
    fn=predict_final_position,
    inputs=gr.Dropdown(choices=pilot_names, label="Selecciona un piloto"),
    outputs="number",
    title="Predicción de Posición Final de F1",
    description="Selecciona un piloto para predecir su posición final en la temporada"
)

# Ejecutar la interfaz
interface.launch()