def collect_data():
    # Simulate data collection
    import pandas as pd
    df = pd.DataFrame({
        'feature1': range(100),
        'feature2': range(100, 200),
        'target': [1 if i % 2 == 0 else 0 for i in range(100)]
    })
    df.to_csv('data/raw.csv', index=False)
    return "Data collected"
