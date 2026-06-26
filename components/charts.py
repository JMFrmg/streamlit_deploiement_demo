import pandas as pd
import plotly.express as px

HOOVER_DATA = ['Hotel_Name', 'Hotel_Address', 'Reviewer_Score']

# Fonction qui renvoie la fig de la carte
def map_fig(df_hotels: pd.DataFrame, review_score_min: float, review_score_max: float):
    fig = px.scatter_map(
        df_hotels,
        lat="lat",
        lon="lng",
        map_style="carto-positron",
        color="Reviewer_Score",
        color_continuous_scale=["Red", "Blue"],
        size="Total_Number_of_Reviews",
        center=dict(lat=48.866667, lon=2.333333),
        zoom=12,
        height=700,
        hover_data=HOOVER_DATA,
        range_color=(review_score_min, review_score_max),
    )
    return fig