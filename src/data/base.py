"""
base.py

Processing of the historical dataset (Kaggle - Student Depression Dataset).
"""

import pandas as pd

from .mapping import DATA_MAPPING
from .schema import METADATA_FEATURES


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
