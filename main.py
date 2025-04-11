import streamlit as st

st.markdown('# Markdown')
st.markdown('## Markdown')
st.markdown('### Markdown')

st.header('Header')
st.subheader('SubHeader')
st.text('Text')
st.caption('Caption')

code_snippet = """
def greet(name):
    return f"Hello, {name}!"
"""
st.code(code_snippet, language="python")