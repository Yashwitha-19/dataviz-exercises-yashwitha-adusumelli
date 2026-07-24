# =====================================================
# Platform Analysis Page
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

st.title("🕹️ Platform Analysis")

st.write("""
Analyze the performance of different gaming platforms based on
the number of released games and total global sales.
""")

st.markdown("---")

# -----------------------------------------------------
# Platform Filter
# -----------------------------------------------------

platforms = sorted(df["Platform"].unique())

selected_platforms = st.multiselect(
    "Select Platform(s)",
    options=platforms,
    default=platforms
)

filtered_df = df[df["Platform"].isin(selected_platforms)]

st.markdown("---")

# -----------------------------------------------------
# Games by Platform
# -----------------------------------------------------

st.subheader("🎮 Number of Games by Platform")

platform_games = (
    filtered_df.groupby("Platform")
    .size()
    .reset_index(name="Number of Games")
    .sort_values("Number of Games", ascending=False)
)

fig = px.bar(
    platform_games,
    x="Platform",
    y="Number of Games",
    color="Platform",
    text="Number of Games",
    title="Games Released by Platform"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False,
    xaxis_title="Platform",
    yaxis_title="Number of Games"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Global Sales by Platform
# -----------------------------------------------------

st.subheader("💰 Global Sales by Platform")

platform_sales = (
    filtered_df.groupby("Platform")["Global_Sales"]
    .sum()
    .reset_index()
    .sort_values("Global_Sales", ascending=False)
)

fig = px.bar(
    platform_sales,
    x="Platform",
    y="Global_Sales",
    color="Platform",
    text_auto=".2f",
    title="Global Sales by Platform"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False,
    xaxis_title="Platform",
    yaxis_title="Global Sales (Millions)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Average Sales Per Game
# -----------------------------------------------------

st.subheader("📈 Average Sales per Game")

avg_sales = (
    filtered_df.groupby("Platform")["Global_Sales"]
    .mean()
    .reset_index()
    .sort_values("Global_Sales", ascending=False)
)

fig = px.bar(
    avg_sales,
    x="Platform",
    y="Global_Sales",
    color="Platform",
    text_auto=".2f",
    title="Average Global Sales per Game"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False,
    xaxis_title="Platform",
    yaxis_title="Average Sales (Millions)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Top Platforms Table
# -----------------------------------------------------

st.subheader("🏆 Platform Statistics")

platform_table = (
    filtered_df.groupby("Platform")
    .agg(
        Games=("Name", "count"),
        Total_Global_Sales=("Global_Sales", "sum"),
        Average_Global_Sales=("Global_Sales", "mean"),
        Publishers=("Publisher", "nunique")
    )
    .sort_values("Total_Global_Sales", ascending=False)
)

st.dataframe(
    platform_table,
    use_container_width=True
)

st.markdown("---")

# -----------------------------------------------------
# Top 10 Platforms
# -----------------------------------------------------

st.subheader("🥇 Top 10 Platforms by Global Sales")

top10 = platform_sales.head(10)

fig = px.bar(
    top10,
    x="Platform",
    y="Global_Sales",
    color="Platform",
    text_auto=".2f",
    title="Top 10 Platforms"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Platform Market Share
# -----------------------------------------------------

st.subheader("🥧 Platform Market Share")

fig = px.pie(
    top10,
    names="Platform",
    values="Global_Sales",
    hole=0.45,
    title="Top Platform Share"
)

fig.update_layout(title_x=0.5)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Insights
# -----------------------------------------------------

st.subheader("📌 Insights")

best_platform = platform_sales.iloc[0]["Platform"]
sales = platform_sales.iloc[0]["Global_Sales"]

games = platform_games.loc[
    platform_games["Platform"] == best_platform,
    "Number of Games"
].values[0]

st.success(f"""
### Best Performing Platform

🎮 **Platform:** {best_platform}

💰 **Global Sales:** {sales:.2f} million copies

📦 **Games Released:** {games}

This platform generated the highest total sales in the selected dataset.
""")