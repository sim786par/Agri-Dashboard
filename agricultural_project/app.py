import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import json
import requests

# -------------------------------
# LOAD FILES
# -------------------------------
rf = joblib.load("randomforest_regressor.pkl")
preprocessor = joblib.load("preprocessor.pkl")
df = pd.read_csv("crop_yield.csv")

st.set_page_config(page_title="Agri Dashboard", layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1 style='text-align:center; color:#4CAF50;'>🌾 Smart Agriculture Dashboard</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# KPI CARDS
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🌱 Avg Yield", round(df['Yield'].mean(),2))
col2.metric("🌧️ Avg Rainfall", round(df['Annual_Rainfall'].mean(),2))
col3.metric("🧪 Avg Fertilizer", round(df['Fertilizer'].mean(),2))

st.markdown("---")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

selected_state = st.sidebar.multiselect(
    "Select State",
    df['State'].unique(),
    default=df['State'].unique()
)

selected_crop = st.sidebar.multiselect(
    "Select Crop",
    df['Crop'].unique(),
    default=df['Crop'].unique()
)

selected_season = st.sidebar.multiselect(
    "Select Season",
    df['Season'].unique(),
    default=df['Season'].unique()
)

# Apply filters
filtered_df = df[
    (df['State'].isin(selected_state)) &
    (df['Crop'].isin(selected_crop)) &
    (df['Season'].isin(selected_season))
]

# -------------------------------
# RAINFALL VS YIELD
# -------------------------------
st.subheader("🌧️ Rainfall vs Yield")

fig2 = px.scatter(
    filtered_df,
    x='Annual_Rainfall',
    y='Yield',
    color='Season',
    color_discrete_sequence=px.colors.qualitative.Set2
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# FEATURE IMPORTANCE
# -------------------------------
st.subheader("🔥 Feature Importance")

importance = rf.feature_importances_
feature_names = preprocessor.get_feature_names_out()

imp_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
}).sort_values(by='Importance', ascending=False)

imp_df['Feature'] = imp_df['Feature'].str.replace('onehotencoder__', '')

fig3 = px.bar(
    imp_df.head(10),
    x='Importance',
    y='Feature',
    orientation='h',
    color='Importance',
    color_continuous_scale='viridis'
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# PREDICTION SECTION
# -------------------------------
st.sidebar.markdown("---")
st.sidebar.header("🔮 Predict Yield")

crop = st.sidebar.selectbox("Crop", df['Crop'].unique())
season = st.sidebar.selectbox("Season", df['Season'].unique())
state = st.sidebar.selectbox("State", df['State'].unique())

year = st.sidebar.number_input("Year", 1997, 2025, 2020)
area = st.sidebar.number_input("Area", 0.0, 1000000.0, 100.0)
production = st.sidebar.number_input("Production", 0.0, 10000000.0, 1000.0)
rainfall = st.sidebar.number_input("Rainfall", 0.0, 5000.0, 1000.0)
fertilizer = st.sidebar.number_input("Fertilizer", 0.0, 10000000.0, 500.0)
pesticide = st.sidebar.number_input("Pesticide", 0.0, 100000.0, 50.0)

def predict():
    input_df = pd.DataFrame([{
        'Crop': crop,
        'Crop_Year': year,
        'Season': season,
        'State': state,
        'Area': area,
        'Production': production,
        'Annual_Rainfall': rainfall,
        'Fertilizer': fertilizer,
        'Pesticide': pesticide
    }])

    transformed = preprocessor.transform(input_df)
    return rf.predict(transformed)[0]

if st.sidebar.button("Predict"):
    result = predict()

    st.markdown(f"""
    <div style="background-color:#1E1E1E;padding:20px;border-radius:10px;text-align:center;">
        <h2 style="color:#4CAF50;">🌱 Predicted Yield</h2>
        <h1 style="color:white;">{result:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.markdown("---")
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head())