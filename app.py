# app.py
import streamlit as st
from pages import home, insights, graphs, pdf_export

pages = {
    "Home": home.display,
    "Insights": insights.display,
    "Graphs": graphs.display,
    "PDF Export": pdf_export.display
}

st.set_page_config(page_title="Multi-Page App", layout="wide")

col1, col2, col3, col4 = st.columns(4)

if col1.button("Home"):
    st.session_state.page = "Home"
if col2.button("Insights"):
    st.session_state.page = "Insights"
if col3.button("Graphs"):
    st.session_state.page = "Graphs"
if col4.button("PDF Export"):
    st.session_state.page = "PDF Export"

page = st.session_state.page if st.session_state.page else "Home"

pages[page]()
