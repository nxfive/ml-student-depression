def prepare_grid(params: dict[str, list]) -> dict[str, list]:
    """
    Prepares a parameter grid with the 'model__' namespace for 
    use in an sklearn Pipeline.
    """
    return {f"model__{k}": v for (k, v) in params.items()}
