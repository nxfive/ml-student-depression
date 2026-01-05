import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline


def run_pipeline(
    pipeline: Pipeline,
    param_grid: dict[str, list],
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Run a pipeline with hyperparameter tuning using GridSearchCV.
    """
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    grid_search = GridSearchCV(pipeline, param_grid, cv=skf, scoring="accuracy")
    grid_search.fit(X_train, y_train)

    y_train_pred = grid_search.best_estimator_.predict(X_train)
    y_test_pred = grid_search.best_estimator_.predict(X_test)
    return y_train_pred, y_test_pred
