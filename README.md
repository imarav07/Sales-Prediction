# Sales-Prediction

## Main Notebook

```
├── notebooks/                
│   ├── preprocessing_feature_engineering.ipynb
```

## Overview
This project aims to develop a robust machine learning model to predict retail store sales based on historical data and various influencing factors. By leveraging advanced algorithms like XGBoost and LightGBM, the model assists businesses in forecasting future sales, optimizing inventory management, and making informed strategic decisions.

## Data Dictionary
```
Feature | Description

Store | Unique identifier for each store
Date | Specific date of the sales record
Weekly_Sales | Sales amount for the given store and date
Holiday_Flag | Indicates whether the week includes a holiday (1 = Yes, 0 = No)
Temperature | Average temperature for the week
Fuel_Price | Cost of fuel in the region
CPI | Consumer Price Index
Unemployment | Unemployment rate in the region
IsHoliday | Boolean flag indicating if the day is a holiday
```

## Strategic Plan of Action

The project follows a structured approach to ensure accurate and reliable sales predictions:
### 1. Data Collection & Exploration
    Gather historical sales data from various stores.
    Perform exploratory data analysis to understand data distributions and identify anomalies.
### 2. Data Preprocessing
    Handle missing values and outliers.
    Encode categorical variables appropriately.
    Feature engineering to create new informative features.

### 3. Model Development
    Split data into training and testing sets.
    Train models using XGBoost and LightGBM algorithms.
    Perform hyperparameter tuning using GridSearchCV for optimal performance.

### 4. Model Evaluation
    Evaluate models using metrics like MAE, RMSE, and R² score.
    Compare model performances and select the best-performing model.
    Explain the model outputs using SHAP and feature importances.

## Project Structure

```
credit_risk/
├── data/                     # Directory for raw and processed data files
│   ├── (All data files)
├── notebooks/                # Jupyter notebooks for analysis and experimentation
│   ├── data_exploration.ipynb
│   ├── preprocessing_feature_engineering.ipynb
├── utils/                   # utility files across the project
│   ├── (All utils)
├── config.yaml               # Configuration parameters of project
├── README.md                 # Project overview and documentation
```

## Model Accuracies

```
Model     |   MAE    |   RMSE   |   R² Score
XGBoost   | 33255.61 | 53671.15 |   0.9909
LightGBM  | 33249.18 | 53580.08 |   0.9909
```
