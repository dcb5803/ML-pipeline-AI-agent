def evaluate_model():
    import mlflow
    import mlflow.sklearn
    import pandas as pd

    df = pd.read_csv('data/processed.csv')
    X = df[['feature1', 'feature2']]
    y = df['target']

    model = mlflow.sklearn.load_model("models:/MLPipeline/Production")
    acc = model.score(X, y)
    with open("logs/performance.txt", "w") as f:
        f.write(f"accuracy: {acc}")
    return f"Model accuracy: {acc}"
