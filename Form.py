import streamlit as st

st.header("Contact Form")

form = st.form(key = 'contact_form', clear_on_submit=True)

age = form.number_input(label = 'Enter your age', min_value=1,max_value=99)

submit_button = form.form_submit_button(label='Submit Age')

if submit_button:
    st.write('Your age was submitted successfully')