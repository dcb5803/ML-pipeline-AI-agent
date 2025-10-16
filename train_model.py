def train_model():
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    import mlflow
    import mlflow.sklearn

    df = pd.read_csv('data/processed.csv')
    X = df[['feature1', 'feature2']]
    y = df['target']

    model = LogisticRegression()
    model.fit(X, y)

    mlflow.set_experiment("MLPipeline")
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "model")
        mlflow.log_metric("accuracy", model.score(X, y))

    return "Model trained and logged"
