import streamlit as st
import requests

response = requests.get(
    "https://httpbin.org/json"
)

st.write("Status Code:", response.status_code)
st.json(response.json())
