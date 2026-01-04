gradient_boosting_grid = {
    "n_estimators": [50, 100, 150, 200],
    "learning_rate": [0.001, 0.01, 0.1],
    "max_depth": [3, 5, 7, 11],
}

k_nearest_neighbors_grid = {
    "n_neighbors": [3, 5, 7, 11],
    "weights": ["uniform", "distance"],
    "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
    "leaf_size": [10, 15, 20, 25, 30],
}

logistic_regression = {
    "penalty": ["l1", "l2", "elasticnet"],
    "c": [0.5, 0.8, 1.0, 1.3],
    "fit_intercept": [True, False],
    "solver": ["saga"],
}

random_forest = {
    "n_estimators": [50, 100, 150, 200],
    "max_depth": [3, 5, 7, 11],
    "min_samples_split": [14, 20, 34],
    "min_samples_leaf": [7, 10, 12],
    "max_features": ["sqrt", "log2", None],
}
