import streamlit as st
import streamlit.components.v1 as components

def display():
    with open('abt.html', 'r') as html_file:
        html_content = html_file.read()
    components.html(html_content, height=2000, scrolling=True)