import streamlit as st
import requests

st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

name_on_order = st.text_input("Name on Smoothie")

st.write("The name on your Smoothie will be", name_on_order)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    ["Apple", "Banana", "Lime", "Mango", "Watermelon"],
    max_selections=5
)

if ingredients_list:

    ingredients_string = ""

for fruit_chosen in ingredients_list:

    ingredients_string += fruit_chosen + " "

    search_on = pd_df.loc[
        pd_df['FRUIT_NAME'] == fruit_chosen,
        'SEARCH_ON'
    ].iloc[0]

    st.write(
        'The search value for ',
        fruit_chosen,
        ' is ',
        search_on,
        '.'
    )

    st.subheader(
        fruit_chosen + ' Nutrition Information'
    )

    fruitvice_response = requests.get(
        "https://my.smoothiefroot.com/api/fruit/" + search_on
    )

    st.dataframe(
        data=fruitvice_response.json(),
        use_container_width=True
    )
