import streamlit as st
import pandas as pd
import plotly.express as px

from data.loader import load_reviews
from data.preprocessor import group_hotels
from components.charts import map_fig


st.set_page_config(page_title="Analyse des commentaires clients des hôtels", layout="wide")

st.title("Analyse des commentaires clients des hôtels")

df_reviews = load_reviews()
df_hotels = group_hotels(df_reviews)

# Sidebar
with st.sidebar:
    st.title("Filtrage des données")
    score_min = df_reviews.Reviewer_Score.min()
    score_max = df_reviews.Reviewer_Score.max()
    selected_score_min, selected_score_max = st.slider(
        "Notes minimales et maximales des commentaires", score_min, score_max, (score_min, score_max), step=0.1, help="Choisissez des notes"
    )
    hotel_score_min = df_hotels.Reviewer_Score.min()
    hotel_score_max = df_hotels.Reviewer_Score.max()
    selected_hotel_score_min, selected_hotel_score_max = st.slider(
        "Notes minimales et maximales des hôtels", hotel_score_min, hotel_score_max, (hotel_score_min, hotel_score_max), step=0.1, help="Choisissez des notes"
    )


# Filtrage des données
df_hotels = df_hotels.loc[(df_hotels.Reviewer_Score >= hotel_score_min) & (df_hotels.Reviewer_Score <= hotel_score_max), :]
df_reviews = df_reviews.loc[df_reviews.Hotel_Name.isin(df_hotels.Hotel_Name)]
df_reviews = df_reviews.loc[(df_reviews.Reviewer_Score >= selected_score_min) & (df_reviews.Reviewer_Score <= selected_score_max), :]
df_hotels = group_hotels(df_reviews)  # Recalcul de l'aggrégation avec la df_reviews filtrée

st.space(size="medium") # Espace après le titre

if not df_hotels.empty: # Vérifier que la df_hotels n'est pas vide
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Note moyenne", f"{df_reviews['Reviewer_Score'].mean():,.2f}")
    with col2:
        st.metric("Note max", f"{df_hotels.Reviewer_Score.max():,.2f}")
    with col3:
        st.metric("Note min", f"{df_hotels.Reviewer_Score.min():,.2f}")
    
    fig = map_fig(df_hotels, score_min, score_max)
    st.plotly_chart(fig)
else:
    st.error("La dataframe est vide ! Veuillez sélectionner d'autres filtres.")

