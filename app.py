import streamlit as st

import numpy as np
import pandas as pd
import datetime

import requests

'''
# Predict your taxi fare!
'''

key = "2012-10-06%2012:10:20.0000001"

date_time = st.text_input("Date Time")

#time = st.text_input("Time")

pickup_lon = st.text_input("Pickup longitude")

pickup_lat = st.text_input("Pickup latitude")

dropoff_lon = st.text_input("Dropoff longitude")

dropoff_lat = st.text_input("Dropoff latitude")

passenger_count = st.number_input("Number of passengers", 1, 8)

button = st.button('Go!')

call_dict = {
    'key': key,
    'pickup_datetime': date_time,
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count
    }


url = 'http://taxifare.lewagon.ai/predict_fare/'

if url == 'http://taxifare.lewagon.ai/predict_fare/':
    #response = requests.get(f"{url}predict_fare/?key={call_dict['key']}&pickup_datetime={call_dict['date']}%{time}&pickup_longitude={call_dict['pickup_lon']}&pickup_latitude={call_dict['pickup_lat']}&dropoff_longitude={call_dict['dropoff_lon']}&dropoff_latitude={call_dict['dropoff_lat']}&passenger_count={call_dict['passenger_count']}")
    if button == 1:
        prediction = requests.get(url, params=call_dict).json()['prediction']
        st.markdown(f"## Your fare will cost {prediction}")
    else:
        st.markdown("## Press the button!")
