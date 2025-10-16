def preprocess_data():
    import pandas as pd
    df = pd.read_csv('data/raw.csv')
    df['feature1'] = df['feature1'] / 100
    df['feature2'] = df['feature2'] / 200
    df.to_csv('data/processed.csv', index=False)
    return "Data preprocessed"
