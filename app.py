import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
@st.cache_resource
def load_model():
    with open('battery_lifecycle_random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Maximum RUL (assuming the maximum RUL is the total number of cycles, e.g., 10000)
MAX_RUL = 10000

# Create a function to make predictions and convert to percentage
def predict_rul(temperature, voltage, current, internal_resistance, charge_time, discharge_time, soc, soh, dod, ambient_humidity):
    features = pd.DataFrame({
        'Temperature': [temperature],
        'Voltage': [voltage],
        'Current': [current],
        'Internal_Resistance': [internal_resistance],
        'Charge_Time': [charge_time],
        'Discharge_Time': [discharge_time],
        'SOC': [soc],
        'SOH': [soh],
        'DOD': [dod],
        'Ambient_Humidity': [ambient_humidity]
    })
    prediction = model.predict(features)
    remaining_cycles = prediction[0]
    percentage_rul = (remaining_cycles / MAX_RUL) * 100
    return remaining_cycles, percentage_rul

# Create the Streamlit web app
st.title('Battery Remaining Useful Life Predictor')

st.write("""
Enter the battery features to predict the Remaining Useful Life (RUL) as both a percentage and in terms of remaining life cycles.
""")

# Add input fields for user to enter battery features
temperature = st.number_input('Temperature (°C)', value=25.0)
voltage = st.number_input('Voltage (V)', value=4.0)
current = st.number_input('Current (A)', value=1.5)
internal_resistance = st.number_input('Internal Resistance', value=0.1)
charge_time = st.number_input('Charge Time (minutes)', value=60)
discharge_time = st.number_input('Discharge Time (minutes)', value=120)
soc = st.number_input('State of Charge (SOC)', value=100.0)
soh = st.number_input('State of Health (SOH)', value=100.0)
dod = st.number_input('Depth of Discharge (DOD)', value=0.0)
ambient_humidity = st.number_input('Ambient Humidity (%)', value=40.0)

# Predict RUL as a percentage and remaining cycles when user clicks the button
if st.button('Predict'):
    remaining_cycles, rul_percentage = predict_rul(
        temperature, voltage, current, internal_resistance, 
        charge_time, discharge_time, soc, soh, dod, ambient_humidity
    )
    st.success(f'Predicted Remaining Useful Life (RUL): {rul_percentage:.2f}%  [around {remaining_cycles:.2f} cycles remaining]')
