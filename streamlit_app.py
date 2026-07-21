import streamlit as st
import requests

st.title("🍓 Fernanda Smoothies")

response = requests.get("https://httpbin.org/get")

st.write("Status Code:", response.status_code)
