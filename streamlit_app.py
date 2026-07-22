import streamlit as st
import requests
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

st.write("""
Choose the fruits you want in your custom Smoothie!
""")

name_on_order = st.text_input(
    "Name on Smoothie"
)

st.write(
    "The name on your Smoothie will be",
    name_on_order
)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    pd_df["FRUIT_NAME"].tolist(),
    max_selections=5
)

st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    ["Apple", "Banana", "Blueberry", "Mango", "Watermelon"],
    max_selections=5
)

if ingredients_list:

    for fruit_chosen in ingredients_list:

        st.subheader(
            fruit_chosen + " Nutrition Information"
        )

        response = requests.get(
            "https://my.smoothiefroot.com/api/fruit/" + fruit_chosen
        )

        st.dataframe(
            data=response.json(),
            use_container_width=True
        )
