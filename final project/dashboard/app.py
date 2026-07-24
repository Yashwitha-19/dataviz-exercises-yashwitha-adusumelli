# =====================================================
# Video Game Sales Dashboard
# Main Application
# =====================================================

import streamlit as st
from utils import load_data, get_kpis

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Video Game Sales Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = load_data()

kpis = get_kpis(df)

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

st.sidebar.title("🎮 Dashboard Navigation")

st.sidebar.markdown("""
Use the pages below to explore the dashboard.

### Available Pages

- 📊 Overview
- 🎯 Genres
- 🕹️ Platforms
- 🌍 Regional Analysis
- ⭐ Scores
- ✅ Conclusion
""")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Course:** Data Visualization

    **Project:** Video Game Sales Dashboard

    **Tools Used**
    - Streamlit
    - Plotly
    - Pandas
    """
)

# -----------------------------------------------------
# Dashboard Title
# -----------------------------------------------------

st.title("🎮 Video Game Sales Dashboard")

st.markdown("""
This dashboard analyzes global video game sales using interactive visualizations.

It explores:

- Genre popularity
- Platform performance
- Publisher sales
- Regional trends
- Critic and user scores
- Business insights
""")

st.markdown("---")

# -----------------------------------------------------
# KPI Section
# -----------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🎮 Games",
        f"{kpis['Total Games']:,}"
    )

with col2:
    st.metric(
        "💰 Global Sales",
        f"{kpis['Global Sales']:.2f} M"
    )

with col3:
    st.metric(
        "🏢 Publishers",
        kpis["Publishers"]
    )

with col4:
    st.metric(
        "🕹️ Platforms",
        kpis["Platforms"]
    )

with col5:
    st.metric(
        "🎯 Genres",
        kpis["Genres"]
    )

st.markdown("---")

# -----------------------------------------------------
# Welcome Message
# -----------------------------------------------------

st.header("Welcome!")

st.write("""
This dashboard presents an interactive analysis of the Video Game Sales dataset.

Navigate using the sidebar to explore:

- Overview of the dataset
- Genre analysis
- Platform analysis
- Regional sales comparison
- Critic and user score analysis
- Final conclusions
""")

st.success("Select a page from the sidebar to begin exploring the dashboard.")