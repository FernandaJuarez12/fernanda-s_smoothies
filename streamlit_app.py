import requests

smoothiefroot_response = requests.get(
    "https://smoothiefroot.com/api/fruit/watermelon"
)

st.json(smoothiefroot_response.json())
