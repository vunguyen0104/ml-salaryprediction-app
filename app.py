import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# This must be the first Streamlit command used in your app, and must only be set once. 
st.set_page_config(
    page_title="Software Developer Salary Prediction", 
    page_icon=":chart_with_upwards_trend:", 
    layout="wide"
)

page = st.sidebar.selectbox("Predict or Explore", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)