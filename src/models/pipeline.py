from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.data.features import BINARY, CATEGORICAL, NUMERIC


def create_knn_pipeline() -> Pipeline:
    """
    Create a scikit-learn Pipeline for K-Nearest Neighbors classification.
    """
    preprocessor = ColumnTransformer(
        [
            ("num", StandardScaler(), NUMERIC),
            ("bin", "passthrough", BINARY),
            (
                "cat",
                OneHotEncoder(
                    drop="first", sparse_output=False, handle_unknown="ignore"
                ),
                CATEGORICAL,
            ),
        ]
    )

    return Pipeline([("preprocessor", preprocessor), ("model", KNeighborsClassifier())])


def create_lr_pipeline() -> Pipeline:
    """
    Create a scikit-learn Pipeline for Logistic Regression classification.
    """
    preprocessor = ColumnTransformer(
        [
            ("num", StandardScaler(), NUMERIC),
            ("bin", "passthrough", BINARY),
            (
                "cat",
                OneHotEncoder(
                    drop="first", sparse_output=False, handle_unknown="ignore"
                ),
                CATEGORICAL,
            ),
        ]
    )

    return Pipeline([("preprocessor", preprocessor), ("model", LogisticRegression())])


def create_rf_pipeline() -> Pipeline:
    """
    Create a scikit-learn Pipeline for Random Forest classification.
    """
    preprocessor = ColumnTransformer(
        [
            ("rest", "passthrough", NUMERIC + BINARY),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
        ]
    )

    return Pipeline(
        [("preprocessor", preprocessor), ("model", RandomForestClassifier())]
    )
