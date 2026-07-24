# =====================================================
# Conclusion Page
# =====================================================

import streamlit as st

from utils import load_data

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = load_data()

# -----------------------------------------------------
# Page Title
# -----------------------------------------------------

st.title("✅ Project Conclusion")

st.write("""
This page summarizes the key findings and business insights
obtained from the Video Game Sales dataset analysis.
""")

st.markdown("---")

# -----------------------------------------------------
# Project Summary
# -----------------------------------------------------

st.header("📋 Project Summary")

st.write("""
The Video Game Sales Dashboard provides an interactive analysis of
historical video game sales across different genres, platforms,
publishers, and regions.

Using Streamlit and Plotly, the dashboard enables users to explore
market trends, compare platform performance, evaluate regional sales,
and understand how review scores relate to commercial success.
""")

st.markdown("---")

# -----------------------------------------------------
# Key Findings
# -----------------------------------------------------

st.header("📌 Key Findings")

st.success("""
🎮 Action and Sports are among the most popular genres.

🕹️ Older platforms such as PS2, Wii, DS, and Xbox 360 generated
some of the highest global sales.

🌍 North America contributed the highest overall sales,
followed by Europe.

⭐ Games with higher critic and user scores generally
showed better sales performance, although the relationship
was moderate rather than perfect.

🏢 A small number of publishers dominated the market,
contributing a large share of global sales.
""")

st.markdown("---")

# -----------------------------------------------------
# Business Recommendations
# -----------------------------------------------------

st.header("💡 Business Recommendations")

st.info("""
• Focus game development on high-performing genres such as Action,
Sports, and Shooter games.

• Invest in platforms with historically strong market performance.

• Prioritize releases in North American and European markets.

• Improve game quality to achieve higher critic and user ratings.

• Use regional preferences to design targeted marketing campaigns.
""")

st.markdown("---")

# -----------------------------------------------------
# Technologies Used
# -----------------------------------------------------

st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.write("""
**Programming**

- Python
- Pandas
- NumPy
- Streamlit
""")

with col2:
    st.write("""
**Visualization**

- Plotly Express
- Interactive Dashboard
- CSV Dataset
""")

st.markdown("---")

# -----------------------------------------------------
# Dataset Statistics
# -----------------------------------------------------

st.header("📊 Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Games", len(df))

with col2:
    st.metric("Platforms", df["Platform"].nunique())

with col3:
    st.metric("Genres", df["Genre"].nunique())

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Publishers", df["Publisher"].nunique())

with col2:
    st.metric(
        "Years Covered",
        f"{df['Year_of_Release'].min()} - {df['Year_of_Release'].max()}"
    )

with col3:
    st.metric(
        "Global Sales",
        f"{df['Global_Sales'].sum():.2f} M"
    )

st.markdown("---")

# -----------------------------------------------------
# Final Conclusion
# -----------------------------------------------------

st.header("🎯 Final Conclusion")

st.write("""
This dashboard demonstrates how interactive data visualization can
transform raw sales data into meaningful business insights.

By combining descriptive statistics, interactive charts, and
comparative analysis, users can better understand trends in the
video game industry and make informed decisions based on historical
sales patterns.
""")

st.success("🎉 Thank you for exploring the Video Game Sales Dashboard!")

st.markdown("---")

st.caption(
    "Data Visualization Final Project | Streamlit Dashboard | Video Game Sales Dataset"
)