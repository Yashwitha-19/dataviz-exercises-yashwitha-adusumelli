# =====================================================
# Scores Analysis Page
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

st.title("⭐ Critic & User Score Analysis")

st.write("""
Analyze the relationship between critic scores,
user scores, and global video game sales.
""")

st.markdown("---")

# -----------------------------------------------------
# Remove Missing Values
# -----------------------------------------------------

score_df = df.dropna(subset=["Critic_Score", "User_Score"])

score_df["User_Score"] = score_df["User_Score"].astype(float)

# -----------------------------------------------------
# Genre Filter
# -----------------------------------------------------

genres = sorted(score_df["Genre"].unique())

selected_genres = st.multiselect(
    "Select Genre(s)",
    genres,
    default=genres
)

filtered_df = score_df[score_df["Genre"].isin(selected_genres)]

st.markdown("---")

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "⭐ Average Critic Score",
        f"{filtered_df['Critic_Score'].mean():.1f}"
    )

with col2:
    st.metric(
        "👤 Average User Score",
        f"{filtered_df['User_Score'].mean():.2f}"
    )

with col3:
    st.metric(
        "💰 Average Global Sales",
        f"{filtered_df['Global_Sales'].mean():.2f} M"
    )

st.markdown("---")

# -----------------------------------------------------
# Critic Score Scatter Plot
# -----------------------------------------------------

st.subheader("📊 Critic Score vs Global Sales")

fig = px.scatter(
    filtered_df,
    x="Critic_Score",
    y="Global_Sales",
    color="Genre",
    hover_name="Name",
    size="Global_Sales",
    title="Critic Score vs Global Sales"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# User Score Scatter Plot
# -----------------------------------------------------

st.subheader("📈 User Score vs Global Sales")

fig = px.scatter(
    filtered_df,
    x="User_Score",
    y="Global_Sales",
    color="Genre",
    hover_name="Name",
    size="Global_Sales",
    title="User Score vs Global Sales"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Average Scores by Genre
# -----------------------------------------------------

st.subheader("🎯 Average Scores by Genre")

genre_scores = (
    filtered_df.groupby("Genre")
    .agg(
        Average_Critic=("Critic_Score", "mean"),
        Average_User=("User_Score", "mean")
    )
    .reset_index()
)

fig = px.bar(
    genre_scores,
    x="Genre",
    y=["Average_Critic", "Average_User"],
    barmode="group",
    title="Average Critic and User Scores by Genre"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    xaxis_title="Genre",
    yaxis_title="Average Score"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Correlation
# -----------------------------------------------------

st.subheader("📉 Correlation Analysis")

critic_corr = filtered_df["Critic_Score"].corr(filtered_df["Global_Sales"])
user_corr = filtered_df["User_Score"].corr(filtered_df["Global_Sales"])

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Critic Score Correlation",
        f"{critic_corr:.2f}"
    )

with col2:
    st.metric(
        "User Score Correlation",
        f"{user_corr:.2f}"
    )

# -----------------------------------------------------
# Highest Rated Games
# -----------------------------------------------------

st.subheader("🏆 Highest Rated Games")

top_games = (
    filtered_df[
        [
            "Name",
            "Genre",
            "Platform",
            "Critic_Score",
            "User_Score",
            "Global_Sales"
        ]
    ]
    .sort_values(
        "Critic_Score",
        ascending=False
    )
    .head(15)
)

st.dataframe(
    top_games,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------------------------
# Insights
# -----------------------------------------------------

st.subheader("📌 Key Insights")

st.info(f"""
### Score Analysis Summary

⭐ Average Critic Score: **{filtered_df['Critic_Score'].mean():.1f}**

👤 Average User Score: **{filtered_df['User_Score'].mean():.2f}**

📈 Critic Score Correlation: **{critic_corr:.2f}**

📈 User Score Correlation: **{user_corr:.2f}**

Higher correlation values indicate a stronger relationship
between review scores and global sales.
""")