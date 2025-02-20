import streamlit as st
import pandas as pd
import numpy as np
import pickle
import math

st.title('Predicting Overnight Visitors with Project Model')
st.subheader('Please enter the following details to predict the number of Overnight Visitors:')
col1, col2 = st.columns(2)
with col1:        
    year = st.radio(
        "Select Year",
        key="visibility",
        options=["2020", "2021", "2022", "2023", "2024", "2025"],
        horizontal=True,
    )
    AirTravel = st.slider('Air Travel', 0, 200, 0)
    LandTravel = st.slider('Land Travel', 0, 200, 0)
    TravelExpendeture = st.slider('Travel Expendeture', 0, 1000, 0)
with col2:
    PassengerTransportExpendeture = st.slider('Passenger Transport Expendeture', 0, 10000, 0)
    NumberOfEstablishments = st.slider('Number Of Establishments', 0, 10000, 0)
    NumberOfRooms = st.slider('Number Of Rooms', 0, 10000, 0)
    NumberOfBedPlaces = st.slider('Number Of Bed Places', 0, 10000, 0)

if st.button("Predict"):
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)       
        prediction = loaded_model.predict(np.array([int(year), AirTravel, LandTravel, TravelExpendeture, PassengerTransportExpendeture, NumberOfEstablishments, NumberOfRooms, NumberOfBedPlaces]).reshape(1, -1));
        st.info('Prediction for Overnight Visitors: {}'.format(math.ceil(prediction[0])))   