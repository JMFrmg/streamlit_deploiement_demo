import streamlit as st
import pandas as pd

def group_hotels(df_reviews: pd.DataFrame) -> pd.DataFrame:
    group_column = "Hotel_Name"
    agg = {
        "Hotel_Address": "first",
        "Reviewer_Score": "mean",
        "Total_Number_of_Reviews": "sum",
        "lat": "first",
        "lng": "first"}
    df_hotels = df_reviews.groupby(group_column).agg(agg)
    return df_hotels.reset_index()
