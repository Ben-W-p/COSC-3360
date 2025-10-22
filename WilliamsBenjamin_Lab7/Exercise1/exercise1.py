import pandas as pd
from datetime import date

def mySplit(line: str):
    s = line.strip()

    i = len(s) - 1
    numeric_chars = []

    while i >= 0:
        ch = s[i]
        if ch.isdigit() or ch == '.':
            numeric_chars.append(ch)
        elif ch == '-' and len(numeric_chars) > 0:
            numeric_chars.append(ch)
            i -= 1
            break
        else:
            break #Once we have reached a space or a letter, we have all we need
        i -= 1

    price_str = ''.join(reversed(numeric_chars)).strip()

    name_part = s[:i+1].rstrip()

    if not name_part and price_str != '':
        name_part = ''

    price_val = None
    if price_str:
        price_val = float(price_str)

    return name_part, price_val, price_str


df = pd.DataFrame(columns=['Product Name', 'Price'])
currentDate = date.today()
out_path = f"myReceipt_{currentDate}.csv"

print("Enter items like:  fresh bread 3.51")
print("Type -999 for the product name OR the price to finish.\n")

while True:
    line = input("Item: ").strip()
    if not line:
        continue

    name, price, price_str = mySplit(line)

    if name == "-999" or price_str == "-999":
        print("Done. Writing CSV...")
        break

    df.loc[len(df)] = [name, float(price)]


df.to_csv(out_path, index=False)
print(f"Saved {len(df)} rows to {out_path}")
