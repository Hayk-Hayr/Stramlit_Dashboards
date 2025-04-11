import streamlit as st
import datetime as dt

st.header('All about dropdowns')

car_manufacturer = ['Ford', 'Lexus', 'Toyota', 'VW', 'Audi']

selected_car = st.selectbox(label='Car Manufacturer', options = car_manufacturer, label_visibility='collapsed', placeholder='Select a manufacturer')

selected_options = st.multiselect(label = "Select favourites", options = car_manufacturer, label_visibility='collapsed', placeholder='Select top 3 manufacturers', max_selections=3)

basic_slider = st.slider(label = 'basic slider', min_value=1, max_value=100, value=50)

range_slider = st.slider(label = 'range slider', min_value=1, max_value=100, value=(50, 70))

date_slider = st.slider(label = 'Select a Date', min_value=dt.date(2023, 1, 2), max_value=dt.date(2024, 12, 31), value=(dt.date(2024, 1, 1), dt.date(2024, 2, 1)), format="DD/MM/YYYY")

number_input = st.number_input(label = 'Enter number', min_value=1, max_value=100, value=50)

sidebar_number_input = st.sidebar.number_input(label='Enter number', min_value=0, max_value=100,value=50, step=5)

st.write(sidebar_number_input)