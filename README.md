# RealEstate-CampX-

🏠 Real Estate Price Prediction & Recommendation System
A full-stack machine learning project built as part of the CampusX Capstone, aimed at predicting property prices, analyzing trends, and recommending similar flats based on user preferences and location in Gurgaon.

## Features
🔹 Multi-page Streamlit App:

Page 1: Geomap Viewer – Interactive Plotly map of Gurgaon showing price per sqft

Page 2: Price Prediction – User inputs → Real-time prediction using Random Forest

Page 3: Analytics Dashboard – Charts, plots, and trend insights

Page 4: Recommender System – Suggests similar properties + shows landmarks in given radius

Deployed using Streamlit

🔹 Robust Feature Selection:

Combined results from 8 methods: Correlation, RFE, Lasso, SHAP, etc.

🔹 Custom Recommendation Engine:

Adjustable weights for similarity by price, location, or size

Nearby landmarks calculated from geo-coordinates

## Data Preprocessing Highlights
Unified area types: Super Built-up, Carpet, Built-up

Converted units (e.g., sqm → sqft)

Imputed missing values intelligently (e.g., float for numerical, large values for missing distances)

Manual corrections for price/area inconsistencies

## Feature Selection Techniques
✔️ Pearson Correlation

✔️ Random Forest Importance

✔️ Gradient Boosting

✔️ Permutation Importance

✔️ Lasso Regularization

✔️ RFE (Recursive Feature Elimination)

✔️ Logistic Regression Coefficients

✔️ SHAP Values

Final features were selected by averaging scores across techniques for reliability.

## Final Model
Random Forest Regressor selected for:

Non-linear capability

Handling of encoded features

Good performance on validation data


## Workflow Overview

Raw Data → Cleaning & Preprocessing → Feature Engineering → Feature Selection 
→ Model Training → Pipeline Building → Visualizations → Deployment

## Visualizations
📍 Geomap with Plotly Mapbox

📊 Boxplots (Bedrooms vs Price)

📉 Area vs Price scatter

🧱 Pie charts, histograms, word maps
