import streamlit as st

tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
    st.header('This is tab 1')

with tab2:
    st.header('This is tab 2')

with tab3:
    st.header('This is tab 3')