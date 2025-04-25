import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple, Any, Union
from sklearn.preprocessing import StandardScaler

def missing_values_treatment(df: pd.DataFrame, config: Dict) -> pd.DataFrame:
    """
    This function is used to treat the missing values in the dataset
    """
    columns = config.keys()
    print(columns)
    for _ in columns:
        replace_value = config.get(_)
        df[_] = df[_].fillna(replace_value)
    return df

def standardize_columns(df: pd.DataFrame, columns: Union[List[str], str]) -> pd.DataFrame:
    """
    This function applies StandardScaler to the specified columns in the dataset
    """
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def create_date_variables(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Function to create date variables from the date column
    """
    # Convert the date column to datetime format
    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True)

    # Create new columns for year, month, day, and day of week
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['day'] = df[date_col].dt.day
    return df