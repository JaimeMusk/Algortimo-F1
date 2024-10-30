import gradio as gr
import joblib
import pandas as pd

# Cargar el modelo
model = joblib.load("models/modelo_random_forest_f1.pkl")

# Cargar los datos necesarios
df_pilot_avg = pd.read_csv("ruta/a/tu/archivo.csv")  # Proporciona la ruta correcta

def predict_final_position(pilot_name):
    data = df_pilot_avg[df_pilot_avg['driver'] == pilot_name]
    input_data = data[['points', 'average_position', 'dnf_count']].values
    prediction = model.predict(input_data)
    return f"La posición final predicha para {pilot_name} es: {int(prediction[0])}"

# Configurar la interfaz de Gradio
interface = gr.Interface(
    fn=predict_final_position,
    inputs=gr.Dropdown(choices=df_pilot_avg['driver'].tolist(), label="Selecciona un piloto"),
    outputs="text",
    title="F1 Final Position Predictor",
    description="Selecciona un piloto para predecir su posición final en el campeonato 2024."
)

# Ejecutar la aplicación
if __name__ == "__main__":
    interface.launch()
