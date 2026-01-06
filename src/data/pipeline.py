import pandas as pd

from .base import (create_binary_column, create_cgpa_category,
                   create_degree_level, csv_to_dataframe, drop_features,
                   map_columns)
from .preprocessing import remove_nan


def data_pipeline() -> pd.DataFrame:
    """
    Run the full data pipeline:
    - loads CSV
    - maps/renames columns
    - drops unnecessary features
    - creates degree & CGPA categories
    - creates binary columns
    - removes NaNs
    """
    return (
        csv_to_dataframe()
        .pipe(map_columns)
        .pipe(drop_features)
        .pipe(create_degree_level)
        .pipe(create_cgpa_category)
        .pipe(create_binary_column)
        .pipe(remove_nan)
    )
