import streamlit as st
import requests
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

session = get_active_session()

...

if ingredients_list:

    ingredients_string = ""

    for fruit_chosen in ingredients_list:

        ingredients_string += fruit_chosen + " "

        smoothiefroot_response = requests.get(
            "https://my.smoothiefroot.com/api/fruit/watermelon"
        )

        sf_df = st.dataframe(
            data=smoothiefroot_response.json(),
            use_container_width=True
        )

    my_insert_stmt = """
    INSERT INTO smoothies.public.orders
    (ingredients, name_on_order)
    VALUES
    ('""" + ingredients_string + """','""" + name_on_order + """')
    """

    if st.button("Submit order"):

        session.sql(my_insert_stmt).collect()

        st.success(
            f"Your Smoothie is ordered, {name_on_order}!",
            icon="✅"
        )
