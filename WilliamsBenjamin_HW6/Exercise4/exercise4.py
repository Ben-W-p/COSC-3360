import numpy as np
import pandas as pd

grades_dict = {
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}

df = pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])

def my_describe(df: pd.DataFrame):
    rows = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    summary = {}

    for col in df.columns:
        values = np.array(df[col], dtype=float)
        n = len(values)
        mean = np.mean(values)

        variance = np.sum((values - mean) ** 2) / (n - 1)
        std_dev = np.sqrt(variance)

        p25 = np.percentile(values, 25)
        p50 = np.percentile(values, 50)
        p75 = np.percentile(values, 75)

        summary[col] = [
            n,
            mean,
            std_dev,
            np.min(values),
            p25,
            p50,
            p75,
            np.max(values)
        ]

    result = pd.DataFrame(summary, index=rows)
    return result

print('My describe function results: \n')
print(my_describe(df))

print("\nPandas describe():\n")
print(df.describe())
