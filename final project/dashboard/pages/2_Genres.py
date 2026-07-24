# =====================================================
# Genre Analysis Page
# =====================================================

import streamlit as st
import plotly.express as px

from utils import load_data

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = load_data()

# -----------------------------------------------------
# Page Title
# -----------------------------------------------------

st.title("🎯 Genre Analysis")

st.write("""
Explore the popularity and sales performance of different video game genres.
Use the interactive filter to focus on specific genres.
""")

st.markdown("---")

# -----------------------------------------------------
# Genre Filter
# -----------------------------------------------------

genres = sorted(df["Genre"].unique())

selected_genres = st.multiselect(
    "Select Genre(s)",
    options=genres,
    default=genres
)

filtered_df = df[df["Genre"].isin(selected_genres)]

st.markdown("---")

# -----------------------------------------------------
# Genre Distribution
# -----------------------------------------------------

st.subheader("📊 Number of Games by Genre")

genre_count = (
    filtered_df.groupby("Genre")
    .size()
    .reset_index(name="Number of Games")
    .sort_values("Number of Games", ascending=False)
)

fig = px.bar(
    genre_count,
    x="Genre",
    y="Number of Games",
    color="Genre",
    text="Number of Games",
    title="Distribution of Games Across Genres"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Global Sales by Genre
# -----------------------------------------------------

st.subheader("💰 Global Sales by Genre")

genre_sales = (
    filtered_df.groupby("Genre")["Global_Sales"]
    .sum()
    .reset_index()
    .sort_values("Global_Sales", ascending=False)
)

fig = px.bar(
    genre_sales,
    x="Genre",
    y="Global_Sales",
    color="Genre",
    text_auto=".2f",
    title="Total Global Sales by Genre"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False,
    xaxis_title="Genre",
    yaxis_title="Global Sales (Millions)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Average Sales per Genre
# -----------------------------------------------------

st.subheader("📈 Average Global Sales per Game")

avg_sales = (
    filtered_df.groupby("Genre")["Global_Sales"]
    .mean()
    .reset_index()
    .sort_values("Global_Sales", ascending=False)
)

fig = px.bar(
    avg_sales,
    x="Genre",
    y="Global_Sales",
    color="Genre",
    text_auto=".2f",
    title="Average Global Sales per Game"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False,
    xaxis_title="Genre",
    yaxis_title="Average Sales (Millions)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Top Genres Table
# -----------------------------------------------------

st.subheader("🏆 Genre Statistics")

genre_table = (
    filtered_df.groupby("Genre")
    .agg(
        Games=("Name", "count"),
        Total_Global_Sales=("Global_Sales", "sum"),
        Average_Global_Sales=("Global_Sales", "mean")
    )
    .sort_values("Total_Global_Sales", ascending=False)
)

st.dataframe(
    genre_table,
    use_container_width=True
)

st.markdown("---")

# -----------------------------------------------------
# Pie Chart
# -----------------------------------------------------

st.subheader("🥧 Genre Share")

fig = px.pie(
    genre_sales,
    names="Genre",
    values="Global_Sales",
    hole=0.4,
    title="Share of Global Sales by Genre"
)

fig.update_layout(title_x=0.5)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Insights
# -----------------------------------------------------

st.subheader("📌 Insights")

top_genre = genre_sales.iloc[0]["Genre"]
top_sales = genre_sales.iloc[0]["Global_Sales"]

st.info(
    f"""
    **Top Performing Genre:** **{top_genre}**

    **Total Global Sales:** **{top_sales:.2f} million copies**

    Use the filter above to compare genre performance and identify market trends.
    """
)