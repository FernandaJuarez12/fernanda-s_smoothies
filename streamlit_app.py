import requests
import streamlit as st

url = "https://smoothiefroot.com/api/fruit/watermelon"

response = requests.get(url)

st.write("Status Code:", response.status_code)
st.write("Texto recibido:")
st.text(response.text)
