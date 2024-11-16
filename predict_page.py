import streamlit as st
import pickle


import numpy as np
from datetime import timedelta

def predict_page():
    st.image("weather_app.png", width=150)
    st.title("Project Skywatchers: Weather Forecast App")

    cities = (
        "Sacramento",
        "Los Angeles",
        "New York City",
        "San Diego"
    )

    city = st.selectbox("City", cities)
    date = str(st.date_input("Forecasted Date")+timedelta(days=1))
    ok = st.button("Weather Forecast")
    if ok:
        def load_model():
            with open(f'saved_predictions_{city.lower()}.pkl', 'rb') as file:
                data = pickle.load(file) 
            return data
        data = load_model()
        table = data["predictions"]
        last_date = str(table.index[-1]+timedelta(days=1))
        if last_date<date:
            prediction = round(table["prediction"][-1])
            date=last_date
        else:
            prediction = round(table["prediction"][date])
            actual = round(table["actual"][date])
            error = round(table["diff"][date])
        formatted_date = date[5:10]+'-'+date[0:4]
        st.subheader(f"The predicted max temperature for {formatted_date} is:", divider="blue") 
        st.header(f"{prediction}\N{DEGREE SIGN} Fahrenheit.", divider="blue")

        if last_date==date:
            st.subheader(" ")
            st.subheader(f"The last weather data value is for {last_date[5:9]+str(int(last_date[9])-1)+'-'+last_date[0:4]}.") 
        else:
            st.subheader(" ")
            st.subheader(f"The actual max temperature for {formatted_date} was:", divider="green") 
            st.header(f"{actual}\N{DEGREE SIGN} Fahrenheit.", divider="green")
            st.subheader(" ")
            st.subheader(f"The total error is:", divider="red") 
            st.header(f"{error}\N{DEGREE SIGN} Fahrenheit.", divider="red")