"""
base.py

Processing of the historical dataset (Kaggle - Student Depression Dataset).
"""

from pathlib import Path

import pandas as pd

from .features import BINARY
from .mapping import DATA_MAPPING
from .schema import METADATA_FEATURES


def csv_to_dataframe() -> pd.DataFrame:
    """
    Load the raw student depression dataset from the project data directory.
    """
    project_root = Path(__file__).resolve().parents[2]
    csv_path = project_root / "data" / "raw" / "student_depression_dataset.csv"
    return pd.read_csv(csv_path)


def map_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename DataFrame columns based on a predefined mapping.
    """
    return df.rename(columns=DATA_MAPPING)


def drop_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop metadata or irrelevant columns from the DataFrame.
    """
    return df.drop(columns=METADATA_FEATURES, errors="ignore")


def categorize_degree(degree: str) -> str:
    """
    Map raw degree values into education level categories.
    """
    if pd.isna(degree):
        return "Missing"
    degree = degree.strip().upper()
    if degree.startswith("M") or degree.startswith("P") or degree == "LLM":
        return "Master or Higher"
    elif degree.startswith("B") or degree == "LLB":
        return "Bachelor"
    return "Secondary Level"


def create_degree_level(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create an ordered categorical column representing education level.
    """
    df["degree_level"] = pd.Categorical(
        df["degree"].apply(categorize_degree),
        categories=["Secondary Level", "Bachelor", "Master or Higher"],
        ordered=True,
    )
    return df


def create_cgpa_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bin CGPA values into ordered categorical performance groups.
    """
    df["cgpa_cat"] = pd.Categorical(
        pd.cut(
            df["cgpa"],
            bins=[5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
            labels=["Average", "Above Average", "Good", "Very Good", "Excelent"],
        ),
        ordered=True,
    )


def create_binary_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert binary categorical columns with 'Yes'/'No' values into 0/1 encoding.
    """
    for column_name in BINARY:
        df[column_name] = (df[column_name] == "Yes").astype(int)
    return df
