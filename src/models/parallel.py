import multiprocessing

from joblib import Parallel, delayed
from tqdm import tqdm

from src.data.pipeline import data_pipeline
from src.utils.grid import prepare_grid
from src.utils.metrics import get_metrics
from src.utils.split import split_dataset

from .params import (gradient_boosting_grid, k_nearest_neighbors_grid,
                     logistic_regression_grid, random_forest_grid)
from .pipeline import (create_gb_pipeline, create_knn_pipeline,
                       create_lr_pipeline, create_rf_pipeline)
from .run import run_pipeline

if __name__ == "__main__":
    df = data_pipeline()
    X_train, X_test, y_train, y_test = split_dataset(df)

    pipeline_tasks = [
        (create_gb_pipeline(), prepare_grid(gradient_boosting_grid)),
        (create_knn_pipeline(), prepare_grid(k_nearest_neighbors_grid)),
        (create_lr_pipeline(), prepare_grid(logistic_regression_grid)),
        (create_rf_pipeline(), prepare_grid(random_forest_grid)),
    ]

    n_processes = min(len(pipeline_tasks), multiprocessing.cpu_count())
    results = Parallel(n_jobs=n_processes)(
        delayed(run_pipeline)(pipeline, grid, X_train, X_test, y_train)
        for pipeline, grid in tqdm(pipeline_tasks, desc="Pipelines")
    )
    for y_train_pred, y_test_pred in results:
        print(get_metrics(y_train, y_test, y_train_pred, y_test_pred))
