import streamlit as st

st.set_page_config(
    page_title="Networking · Asier Dorronsoro",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from views.networking import show_networking

show_networking()