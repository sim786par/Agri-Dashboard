# Agri-Dashboard
ML-powered crop yield prediction and agricultural analytics dashboard built with Python, Scikit-Learn, and Streamlit.

## 📌 Overview

This project analyzes agricultural data and predicts crop yield using Machine Learning. The model considers factors such as crop type, season, state, rainfall, fertilizer usage, pesticide usage, area, and production to estimate crop yield.

---
<h2>Dashboard Preview</h2>
<p align = "center">
    <img width="450" alt="preview1" src="https://github.com/user-attachments/assets/1242bb56-c621-47e7-b0d2-448b1ccd84a3" />
    <img width="450" alt="preview2" src="https://github.com/user-attachments/assets/fde35764-471c-4946-8854-f08011a1aebb" />
</p>
<p align = "center">
    <img width="450" alt="preview3" src="https://github.com/user-attachments/assets/89e6cda1-a869-4e98-81ea-b74c516bc7f7" />
    <img width="450" alt="preview4" src="https://github.com/user-attachments/assets/c4133007-3a1b-4f7b-8279-b2a6f567a257" />
</p>

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

## 📂 Project Structure

```text
Agriculture_Crop_Yield_Analysis/
│
├── app.py
├── randomforest_regressor.pkl
├── preprocessor.pkl
├── crop_yield.csv
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── crop_yield_analysis.ipynb
│
├── models/
│   ├── rf.pkl
│   └── preprocessor.pkl
│
└── .streamlit/
    └── config.toml
```

## 📈 Dashboard Features

- Yield Prediction
- State-wise Yield Analysis
- Rainfall Impact Analysis
- Seasonal Variation Analysis
- Feature Importance Visualization
- Interactive Filters

---


## 🔍 Exploratory Data Analysis (EDA)

Performed the following analysis:

- Missing Value Analysis
- Data Cleaning
- Distribution Analysis
- State-wise Yield Analysis
- Crop-wise Production Analysis
- Rainfall Impact Analysis
- Seasonal Variation Analysis
- Correlation Analysis
- Feature Importance Analysis

---
## ⚙️ Data Preprocessing

### Categorical Encoding

Applied One-Hot Encoding on:

- Crop
- Season
- State

### Feature Scaling

Applied StandardScaler on numerical features:

- Crop_Year
- Area
- Production
- Annual_Rainfall
- Fertilizer
- Pesticide

---

## 🤖 Machine Learning Models

The following regression algorithms were tested:

1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. K-Nearest Neighbors Regressor
5. Decision Tree Regressor
6. Random Forest Regressor

---

## 📈 Model Evaluation

### Performance Comparison

| Model | R² Score |
|---------|---------|
| Linear Regression | 0.80 |
| Lasso Regression | 0.80 |
| Ridge Regression | 0.80 |
| KNN Regressor | 0.93 |
| Decision Tree | 0.81 |
| Random Forest | 0.89 |

### Final Tuned Random Forest

```text
MSE: 10787.368266064788
Score : 0.9865366555777888
```

Selected Model:

✅ Random Forest Regressor

Reason:

- High Prediction Accuracy
- Handles Non-Linearity
- Robust Against Overfitting
- Strong Generalization Performance

---

## 📊 Streamlit Dashboard Features

### Dashboard Includes

✅ KPI Cards

- Average Yield
- Average Rainfall
- Average Fertilizer Usage

✅ Interactive Filters

- State
- Crop
- Season

✅ Visualizations

- Top Yield States
- Rainfall vs Yield
- Feature Importance
- Seasonal Analysis
- Crop Analysis

✅ Yield Prediction System

Users can input agricultural parameters and obtain predicted crop yield instantly.

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


## 📌 Business Questions Answered

The dashboard helps answer:

### Yield Analysis

- Which states have highest crop yield?
- Which crops perform best?

### Rainfall Analysis

- How does rainfall affect yield?
- What is the optimal rainfall range?

### Seasonal Analysis

- Which season produces maximum yield?
- Seasonal crop performance trends.

### Resource Optimization

- Fertilizer impact on production.
- Pesticide impact on yield.

### Prediction

- What yield can be expected for a given crop and region?

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
