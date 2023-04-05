import streamlit as st
from utils import render_result
from config import page_config

st.set_page_config(**page_config)
st.title("What's happening on Reddit")

subreddit = st.text_input(
    label="Subreddit",
    placeholder="r/askhistorians or askhistorians",
    help="Type in a subreddit name to filter by",
)


if subreddit:
    tab1, tab2, tab3, tab4 = st.tabs(["Top", "Hot", "New", "Rising"])

    with tab1:
        render_result(st, subreddit, "Top Posts", "top")

    with tab2:
        render_result(st, subreddit, "Hot Posts", "hot")

    with tab3:
        render_result(st, subreddit, "New Posts", "new")

    with tab4:
        render_result(st, subreddit, "Rising Posts", "rising")
