# app/app.py: "Where do you stand?" tool (hello world version)
# Purpose: load the cleaned survey data and (temporarily) check category labels

import pandas as pd
import streamlit as st

st.title("AI-Native or Left Behind?")
st.write("Where do you stand? This tool is under construction.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/clean.csv")
    return df

df = load_data()

st.write("age_group:", df["age_group"].unique().tolist())
st.write("college:", df["college"].unique().tolist())
st.write("job_broad:", df["job_broad"].unique().tolist())