import streamlit as st

column1, column2, column3 = st.columns(3)

with column1:
    st.header('Column1')

with column2:
    st.header('Column2')

with column3:
    st.header('Column3')