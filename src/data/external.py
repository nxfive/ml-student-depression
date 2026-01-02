"""
external.py

Processing of incoming survey data.
"""

import pandas as pd

from .constants import MANUAL_THRESHOLD


def separate_manual_checking(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Splits incoming survey data into automatically processable rows
    and rows requiring manual verification based on missing value ratio.
    """
    row_nan_ratio = df.isna().mean(axis=1)

    df_manual = df[row_nan_ratio > MANUAL_THRESHOLD]
    df_auto = df[row_nan_ratio <= MANUAL_THRESHOLD]
    return df_auto, df_manual
