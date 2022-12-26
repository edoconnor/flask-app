import pandas as pd
import csv

data = pd.read_csv("data.csv")

data = data.rename(columns={'sales ': 'sales'})

# values = df.month.values.tolist()

print(data.columns)
