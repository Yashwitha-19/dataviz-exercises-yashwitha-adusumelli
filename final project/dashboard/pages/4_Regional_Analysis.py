# =====================================================
# Regional Analysis Page
# =====================================================

import streamlit as st
import plotly.express as px
import pandas as pd

from utils import load_data

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = load_data()

# -----------------------------------------------------
# Page Title
# -----------------------------------------------------

st.title("🌍 Regional Sales Analysis")

st.write("""
Compare video game sales across different regions:
North America, Europe, Japan, and Other Regions.
""")

st.markdown("---")

# -----------------------------------------------------
# Genre Filter
# -----------------------------------------------------

genres = sorted(df["Genre"].unique())

selected_genres = st.multiselect(
    "Select Genre(s)",
    genres,
    default=genres
)

filtered_df = df[df["Genre"].isin(selected_genres)]

# -----------------------------------------------------
# Regional Sales Totals
# -----------------------------------------------------

regional_sales = pd.DataFrame({
    "Region": [
        "North America",
        "Europe",
        "Japan",
        "Other Regions"
    ],
    "Sales": [
        filtered_df["NA_Sales"].sum(),
        filtered_df["EU_Sales"].sum(),
        filtered_df["JP_Sales"].sum(),
        filtered_df["Other_Sales"].sum()
    ]
})

st.markdown("---")

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🇺🇸 North America",
        f"{regional_sales.iloc[0]['Sales']:.2f} M"
    )

with col2:
    st.metric(
        "🇪🇺 Europe",
        f"{regional_sales.iloc[1]['Sales']:.2f} M"
    )

with col3:
    st.metric(
        "🇯🇵 Japan",
        f"{regional_sales.iloc[2]['Sales']:.2f} M"
    )

with col4:
    st.metric(
        "🌎 Other",
        f"{regional_sales.iloc[3]['Sales']:.2f} M"
    )

st.markdown("---")

# -----------------------------------------------------
# Regional Sales Bar Chart
# -----------------------------------------------------

st.subheader("📊 Total Sales by Region")

fig = px.bar(
    regional_sales,
    x="Region",
    y="Sales",
    color="Region",
    text_auto=".2f",
    title="Regional Video Game Sales"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=False,
    xaxis_title="Region",
    yaxis_title="Sales (Millions)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Regional Sales Pie Chart
# -----------------------------------------------------

st.subheader("🥧 Regional Market Share")

fig = px.pie(
    regional_sales,
    names="Region",
    values="Sales",
    hole=0.45,
    title="Regional Sales Distribution"
)

fig.update_layout(title_x=0.5)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Genre Sales by Region
# -----------------------------------------------------

st.subheader("📈 Genre Performance Across Regions")

genre_region = (
    filtered_df.groupby("Genre")[
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    ]
    .sum()
    .reset_index()
)

genre_region = genre_region.melt(
    id_vars="Genre",
    var_name="Region",
    value_name="Sales"
)

genre_region["Region"] = genre_region["Region"].replace({
    "NA_Sales": "North America",
    "EU_Sales": "Europe",
    "JP_Sales": "Japan",
    "Other_Sales": "Other Regions"
})

fig = px.bar(
    genre_region,
    x="Genre",
    y="Sales",
    color="Region",
    barmode="group",
    title="Regional Sales by Genre"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Regional Sales Table
# -----------------------------------------------------

st.subheader("📋 Regional Sales Summary")

table = (
    filtered_df[
        [
            "Name",
            "Genre",
            "Platform",
            "NA_Sales",
            "EU_Sales",
            "JP_Sales",
            "Other_Sales",
            "Global_Sales"
        ]
    ]
    .sort_values("Global_Sales", ascending=False)
)

st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------------------------
# Insights
# -----------------------------------------------------

st.subheader("📌 Key Insights")

best_region = regional_sales.sort_values(
    "Sales",
    ascending=False
).iloc[0]

st.success(f"""
### Highest Performing Region

🌍 **{best_region['Region']}**

💰 **Total Sales:** {best_region['Sales']:.2f} million copies

This region generated the highest video game sales
for the selected genres.
""")