import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
st.markdown('# Gapminder Dashboard')
df = pd.read_csv(r'gapminder_data_graphs.csv')
unique_years = list(df['year'].unique())

col, col0, col00= st.columns([1, 1, 1])

with col:
    selected_year = st.slider(label = 'Select Year', min_value= min(unique_years), max_value = max(unique_years))

df_plot = df[df['year'] == selected_year]

avg_gdp = round(df_plot['gdp'].mean(), 2)
avg_life_exp = round(df_plot['life_exp'].mean(), 2)
avg_hdi = round(df_plot['hdi_index'].mean(), 2)

col1, col2, col3 = st.columns([1, 1, 1], )
col1.metric(label = 'Average GDP', value=f"{avg_gdp:,.2f}")
col2.metric(label = 'Average Life Expectancy', value = f"{avg_life_exp:,.2f}")
col3.metric(label = 'Average HDI', value = f"{avg_hdi:,.2f}")

scatter_plot = px.scatter(df_plot, x = 'gdp', y = 'life_exp', color = 'continent', title=f"Plot of GDP vs Life Expectancy in {selected_year}")
st.plotly_chart(scatter_plot)

col4, col5 = st.columns(2)

with col4:
    gdp_box = px.box(df_plot, x = 'continent', y = 'gdp', title = f"Distribution of GDP across the continents in {selected_year}")
    st.plotly_chart(gdp_box)

    life_exp_box = px.box(df_plot, x='continent', y='life_exp', title = f"Distribution of Life Expectancy across the continents in {selected_year}")
    st.plotly_chart(life_exp_box)

    hdi_box = px.box(df_plot, x = 'continent', y = 'hdi_index', title = f"Distribution of HDI across the continents in {selected_year}")
    st.plotly_chart(hdi_box)
with col5:
    gdp_hist = px.histogram(df_plot, x = 'gdp', title = f"Distribution of GDP in {selected_year}")
    st.plotly_chart(gdp_hist)

    life_exp_hist = px.histogram(df_plot, x = 'life_exp', title = f"Distribution of Life Expectancy in {selected_year}")
    st.plotly_chart(life_exp_hist)

    hdi_hist = px.histogram(df_plot, x = 'hdi_index', title = f"Distribution of GDP in {selected_year}")
    st.plotly_chart(hdi_hist)