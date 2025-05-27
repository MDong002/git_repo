print("hello, world!")

msg = "Mo's cafe"

print(msg)


print("test")

import pandas as pd

s = pd.Series([1, 3, 5, None, 6, 8])
print("Pandas Series:")
print(s)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)