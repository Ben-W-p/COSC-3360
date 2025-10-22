import pandas as pd
from datetime import date

currentDate = date.today()
in_path = f"../Exercise1/myReceipt_{currentDate}.csv"

df = pd.read_csv(in_path)
print("Receipt DataFrame:")
print(df, "\n")

total = 0.0
for val in df['Price']:
    total = total + float(val)

print(f"Total cost: ${total:.2f}")

