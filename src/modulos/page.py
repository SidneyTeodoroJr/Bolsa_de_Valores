import streamlit as st

# Essa função personaliza: o layout da página.
def page():
    st.set_page_config(
        page_title="Closing of Shares", # Titulo
        page_icon="src\img\logo.png", # Ícone
        layout="centered", # Centralizando
        initial_sidebar_state="auto", # Barra lateral
    )