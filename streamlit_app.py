import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    "https://smoothiefroot.com/api/fruit/watermelon",
    headers=headers
)

st.write(response.status_code)
st.text(response.text)
