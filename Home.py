import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏠",
)

st.markdown("<h1 style='text-align: center;'>Welcome to the Home page 🏠</h1>", unsafe_allow_html=True)
data = pd.DataFrame({
    'lat': [28.4595],  # Latitude of Gurgaon
    'lon': [77.0266]   # Longitude of Gurgaon
})

st.markdown("<h2 style='text-align: center;'>🗺️ Map of Gurgaon</h2>", unsafe_allow_html=True)
st.map(data)
st.sidebar.success("Select a page here.")




