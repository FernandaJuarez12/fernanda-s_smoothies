import streamlit as st
import requests

st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

st.write("""
Choose the fruits you want in your custom Smoothie!
""")

name_on_order = st.text_input("Name on Smoothie")

st.write("The name on your Smoothie will be", name_on_order)

# API SmoothieFroot

smoothiefroot_response = requests.get(
    "https://my.smoothiefroot.com/api/fruit/watermelon"
)

st.json(smoothiefroot_response.json())
