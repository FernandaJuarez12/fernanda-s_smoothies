import requests
import streamlit as st

url = "https://smoothiefroot.com/api/fruit/watermelon"

try:
    response = requests.get(url)

    st.write("Status Code:", response.status_code)

    st.json(response.json())

except Exception as e:
    st.error(f"Error: {e}")
