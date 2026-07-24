# =====================================================
# Overview Page
# =====================================================

import streamlit as st
import plotly.express as px

from utils import (
    load_data,
    get_kpis,
    top_games,
    games_per_year
)

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = load_data()

kpis = get_kpis(df)

# -----------------------------------------------------
# Page Title
# -----------------------------------------------------

st.title("📊 Overview")

st.write(
    """
    This page provides a summary of the Video Game Sales dataset,
    including key performance indicators, yearly trends, and the
    top-selling video games.
    """
)

st.markdown("---")

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🎮 Games", f"{kpis['Total Games']:,}")

with col2:
    st.metric("💰 Sales", f"{kpis['Global Sales']:.2f} M")

with col3:
    st.metric("🏢 Publishers", kpis["Publishers"])

with col4:
    st.metric("🕹️ Platforms", kpis["Platforms"])

with col5:
    st.metric("🎯 Genres", kpis["Genres"])

st.markdown("---")

# -----------------------------------------------------
# Games Released Per Year
# -----------------------------------------------------

st.subheader("📈 Number of Games Released Per Year")

games_year = games_per_year(df)

fig = px.line(
    games_year,
    x="Year_of_Release",
    y="Number_of_Games",
    markers=True,
    title="Video Game Releases Over Time"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    xaxis_title="Year",
    yaxis_title="Number of Games"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Top Selling Games
# -----------------------------------------------------

st.subheader("🏆 Top 10 Best-Selling Video Games")

top10 = top_games(df)

st.dataframe(
    top10,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# -----------------------------------------------------
# Dataset Preview
# -----------------------------------------------------

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True
)

# -----------------------------------------------------
# Dataset Information
# -----------------------------------------------------

st.subheader("ℹ Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Rows:**", df.shape[0])
    st.write("**Columns:**", df.shape[1])

with col2:
    st.write("**Missing Values:**", df.isnull().sum().sum())
    st.write("**Duplicate Rows:**", df.duplicated().sum())

st.success("Overview page loaded successfully!")