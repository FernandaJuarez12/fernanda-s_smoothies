import streamlit as st
import requests

response = requests.get(
    "https://httpbin.org/json"
)

st.json(response.json())
