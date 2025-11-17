import streamlit as st
import pickle
import numpy as np

# Load the model
with open('lrmodel_sustainable.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Sustainability Checker")

# User inputs
carbon_emission = st.number_input("Carbon emission amount:", min_value=0.0, format="%f")
energy_output = st.number_input("Energy output generated:", min_value=0.0, format="%f")
renewability_index = st.number_input("Renewability index:", min_value=0.0, format="%f")
cost_efficiency = st.number_input("Cost efficiency index:", min_value=0.0, format="%f")

# Predict button
if st.button("Predict"):
    # Prepare input for model
    input_data = np.array([[carbon_emission, energy_output, renewability_index, cost_efficiency]])

    # Make prediction
    prediction = model.predict(input_data)

    # Show result
    if prediction[0] == 1:
        st.success("It's sustainable 🌿")
    else:
        st.info("Not sustainable ⚠️")
