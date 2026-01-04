"""
external.py

Processing of incoming survey data.
"""

import pandas as pd

from .constants import MANUAL_THRESHOLD


def separate_full_rows(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split incoming survey data into rows without missing values and rows with any
    missing values.
    """
    full_rows = df[df.notna().all(axis=1)]
    rows_with_missing = df[df.isna().any(axis=1)]
    return full_rows, rows_with_missing


def separate_manual_checking(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split rows with missing values from survey data into automatically processable
    rows and rows requiring manual verification based on missing value ratio.
    """
    row_nan_ratio = df.isna().mean(axis=1)

    df_manual = df[row_nan_ratio > MANUAL_THRESHOLD]
    df_auto = df[row_nan_ratio <= MANUAL_THRESHOLD]
    return df_auto, df_manual
