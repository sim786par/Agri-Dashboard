# Agri-Dashboard
ML-powered crop yield prediction and agricultural analytics dashboard built with Python, Scikit-Learn, and Streamlit.

## 📌 Overview

This project analyzes agricultural data and predicts crop yield using Machine Learning. The model considers factors such as crop type, season, state, rainfall, fertilizer usage, pesticide usage, area, and production to estimate crop yield.

---

## 🎯 Objectives

- Analyze crop production trends in India.
- Identify factors affecting crop yield.
- Build a machine learning model for yield prediction.
- Develop an interactive Streamlit dashboard for visualization and prediction.

---

## 📊 Dataset

**Source:** Kaggle - Crop Production in India

Features used:
- Crop
- Crop Year
- Season
- State
- Area
- Production
- Annual Rainfall
- Fertilizer
- Pesticide
- Yield (Target)

---

## 🛠 Technologies Used

- Python
- Pandas & NumPy
- Matplotlib & Plotly
- Scikit-Learn
- Streamlit
- Joblib

---

## 🤖 Machine Learning

Models Tested:
- Linear Regression
- Ridge & Lasso Regression
- KNN Regressor
- Decision Tree Regressor
- Random Forest Regressor

### Final Model
**Random Forest Regressor**

Performance:
- R² Score: **0.986**
- Cross Validation Score: **0.955**
- MSE: **10787**

---

## 📈 Dashboard Features

- Yield Prediction
- State-wise Yield Analysis
- Rainfall Impact Analysis
- Seasonal Variation Analysis
- Feature Importance Visualization
- Interactive Filters

---

## 🚀 Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
python -m streamlit run app.py
```

---

## 📂 Project Structure

```text
Agriculture_Crop_Yield_Analysis/
│
├── app.py
├── rf.pkl
├── preprocessor.pkl
├── dataset.csv
├── requirements.txt
└── README.md
```

---

## 📌 Future Enhancements

- Crop Recommendation System
- Weather API Integration
- Fertilizer Recommendation
- Real-Time Agricultural Analytics

---

## 👨‍💻 Author

Simran Parween

Agriculture Crop Yield Analysis & Prediction using Machine Learning and Streamlit.
