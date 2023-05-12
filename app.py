import streamlit as st
import requests
import json

'''
# TaxiFareModel front
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...

#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')

'''
## Please input your ride data to get an estimated price
'''

date = st.date_input("Pick-up date?")
time = st.time_input("Pick-up time?")
pickup_lon = st.text_input("Pick-up longitude?")
pickup_lat = st.text_input("Pick-up latitude?")
dropoff_lon = st.text_input("Drop-off longitude?")
dropoff_lat = st.text_input("Drop-off latitude?")
passenger_count = st.number_input("Passenger count?", 0, 10)

datetime = (str(date) + " " + str(time))
#'''
## Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

#'''

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
#'''
params = {
    'pickup_datetime': datetime,
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count
    }

r = requests.get(url=url, params=params)
byte_string = (r.content.decode('utf-8'))
data = (json.loads(byte_string))
fare = (data['fare'])
st.write(f'Your fare is = ${fare}')
