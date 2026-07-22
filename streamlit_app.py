import streamlit as st
import requests

st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

name_on_order = st.text_input("Name on Smoothie")

st.write("The name on your Smoothie will be", name_on_order)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    ["Apple", "Banana", "Orange", "Mango", "Watermelon"],
    max_selections=5
)

if ingredients_list:

    for fruit_chosen in ingredients_list:

    ingredients_string += fruit_chosen + " "

    st.subheader(fruit_chosen + " Nutrition Information")

    smoothiefroot_response = requests.get(
        "https://my.smoothiefroot.com/api/fruit/" + fruit_chosen
    )

    sf_df = st.dataframe(
        data=smoothiefroot_response.json(),
        use_container_width=True
    )

