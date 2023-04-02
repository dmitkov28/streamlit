import streamlit as st
import json
import httpx

st.write("New page")

data_load_state = st.text("Loading data...")
data = httpx.get("https://www.reddit.com/r/popular.json").json()
data_load_state.text("Loading data...done!")

# Parse JSON string


# Display JSON data in Streamlit
st.write(data)
