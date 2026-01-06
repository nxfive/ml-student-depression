import pandas as pd


def remove_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove all rows with missing values from the DataFrame.
    """
    df = df.dropna()
    return df
