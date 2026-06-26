import streamlit as st
import pandas as pd

@st.cache_data
def load_reviews(): 
    df_reviews = pd.read_csv("data/hotel_reviews_clean.csv", parse_dates=["Review_Date"])
    return df_reviews