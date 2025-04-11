import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
st.markdown('# Auto MPG Dashboard')

tab1, tab2, tab3 = st.tabs(['Origin: 1', 'Origin: 2', 'Origin: 3'])

df = pd.read_csv('clean_auto_mpg.csv')

def page(origin, tab):
    df1 = df[df['origin'] == origin]
    avg_mpg = round(df1['mpg'].mean(), 2)
    avg_displace = round(df1['displacement'].mean(), 2)
    avg_hp = round(df1['horsepower'].mean(), 2)
    avg_weight = round(df1['weight'].mean(), 2)

    with tab:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label = 'AVG MPG', value = f"{avg_mpg:,.2f}")
        col2.metric(label = 'AVG Displacement', value = f"{avg_displace:,.2f}")
        col3.metric(label = 'AVG Horsepower', value = f"{avg_hp:,.2f}")
        col4.metric(label='AVG Weight', value = f"{avg_weight:,.2f}")

        col5, col6 = st.columns([3, 1])
        scat = px.scatter(df1, x = 'weight', y = 'horsepower', title = 'Weight vs HP', color='cylinders', size='cylinders')
        col5.plotly_chart(scat)
        hist = px.histogram(df1, x = 'mpg', title = 'MPG Distribution')
        col6.plotly_chart(hist)
page(1, tab1)
page(2, tab2)
page(3, tab3)