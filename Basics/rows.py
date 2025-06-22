# head() and tail() methods are used to view the first and last few rows of the DataFrame, respectively.
# head(n) returns the first n rows, and tail(n) returns the last n rows.if we not put n in head then it will return 5 rows by default.


import pandas as pd
df = pd.read_json("sample_Data.json")
print("First 10 rows of the DataFrame:")
print(df.head())
print("Last 10 rows of the DataFrame:")
print(df.tail())
# float numbers not acceptable in JSON format, so it will be converted to string