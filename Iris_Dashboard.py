import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit import title

st.set_page_config(layout='wide')

df = pd.read_csv("iris.csv")
unique_species = df['species'].unique()

st.title('Iris Dashboard')

col1, col2 = st.columns(2)

selected_species = col1.selectbox(label = 'Species', options = unique_species, label_visibility='collapsed', placeholder = "Select")
show_hist = col2.checkbox(label = 'Show Histogram', key = 'checkb')

df_plot = df[df['species'] == selected_species]
avg_sep_length = round(df_plot['sepal_length'].mean(), 2)
avg_sep_width = round(df_plot['sepal_width'].mean(), 2)
avg_pet_length = round(df_plot['petal_length'].mean(), 2)
avg_pet_width = round(df_plot['petal_width'].mean(), 2)

col1, col2, col3, col4 = st.columns(4)
col1.metric(label = 'Sepal Length Average', value = avg_sep_length)
col2.metric(label = 'Sepal Width Average', value = avg_sep_width)
col3.metric(label = 'Petal Length Average', value = avg_pet_length)
col4.metric(label = 'Petal Width Average', value = avg_pet_width)

color_map_dict = {species: 'gray' for species in unique_species}
color_map_dict[selected_species] = '#0068c9'
scatter = px.scatter(df, x= 'sepal_length', y = 'sepal_width', size='petal_length', color='species', color_discrete_map = color_map_dict, title='Sepal Length vs Petal Width for Versicolor')
st.plotly_chart(scatter)

col5, col6, col7, col8 = st.columns(4)

if show_hist:
    with col5:
        dist_sep_length = px.histogram(df_plot, x ='sepal_length', title='Distribution of Sepal Length')
        st.plotly_chart(dist_sep_length)
    with col6:
        dist_sep_width = px.histogram(df_plot, x ='sepal_width', title='Distribution of Sepal Width')
        st.plotly_chart(dist_sep_width)
    with col7:
        dist_pet_length = px.histogram(df_plot, x ='petal_length', title='Distribution of Petal Length')
        st.plotly_chart(dist_pet_length)
    with col8:
        dist_pet_width = px.histogram(df_plot, x ='petal_width', title='Distribution of Petal Width')
        st.plotly_chart(dist_pet_width)