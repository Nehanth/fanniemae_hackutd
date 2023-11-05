# app.py
import streamlit as st
from pages import home, insights, graphs, pdf_export

pages = {
    "Home": home.display,
    "Insights": insights.display,

}

st.set_page_config(page_title="Multi-Page App", layout="wide")

if 'page' not in st.session_state:
    st.session_state['page'] = "Home"

col1, col2 = st.columns(2)

if col1.button("Home"):
    st.session_state['page'] = "Home"
if col2.button("Insights"):
    st.session_state['page'] = "Insights"

pages[st.session_state['page']]()
