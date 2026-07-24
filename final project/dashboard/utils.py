# =====================================================
# utils.py
# Utility functions for the Video Game Sales Dashboard
# =====================================================

import streamlit as st
import pandas as pd

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------
@st.cache_data
def load_data():
    """
    Load the cleaned video game sales dataset.
    """

    df = pd.read_csv("data/vgsales_clean.csv")

    return df


# -----------------------------------------------------
# Dashboard KPIs
# -----------------------------------------------------
def get_kpis(df):
    """
    Calculate dashboard KPI values.
    """

    total_games = len(df)

    total_sales = df["Global_Sales"].sum()

    total_publishers = df["Publisher"].nunique()

    total_platforms = df["Platform"].nunique()

    total_genres = df["Genre"].nunique()

    return {
        "Total Games": total_games,
        "Global Sales": total_sales,
        "Publishers": total_publishers,
        "Platforms": total_platforms,
        "Genres": total_genres,
    }


# -----------------------------------------------------
# Top Games
# -----------------------------------------------------
def top_games(df, n=10):
    """
    Return the top-selling games.
    """

    return (
        df.sort_values(
            by="Global_Sales",
            ascending=False
        )[["Name",
           "Platform",
           "Genre",
           "Publisher",
           "Global_Sales"]]
        .head(n)
    )


# -----------------------------------------------------
# Genre Sales
# -----------------------------------------------------
def genre_sales(df):

    return (
        df.groupby("Genre")["Global_Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Global_Sales",
            ascending=False
        )
    )


# -----------------------------------------------------
# Platform Sales
# -----------------------------------------------------
def platform_sales(df):

    return (
        df.groupby("Platform")["Global_Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Global_Sales",
            ascending=False
        )
    )


# -----------------------------------------------------
# Publisher Sales
# -----------------------------------------------------
def publisher_sales(df):

    return (
        df.groupby("Publisher")["Global_Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Global_Sales",
            ascending=False
        )
    )


# -----------------------------------------------------
# Games Per Year
# -----------------------------------------------------
def games_per_year(df):

    return (
        df.groupby("Year_of_Release")
        .size()
        .reset_index(name="Number_of_Games")
    )


# -----------------------------------------------------
# Regional Sales
# -----------------------------------------------------
def regional_sales(df):

    return {
        "North America": df["NA_Sales"].sum(),
        "Europe": df["EU_Sales"].sum(),
        "Japan": df["JP_Sales"].sum(),
        "Other Regions": df["Other_Sales"].sum()
    }