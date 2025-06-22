#what are the names 
# how big is the data set?
# pandas give two ways to nas thi
# shape and column, shape is attribute which return tuples with true values
# df.shape
# df.columns

# select specific column, to solve this we []

# filter rows, we use boolean for this 
# filtered_Rows= df[df["coulumn_name"]] this for accessing rows
# filtered_Rows = df[df["salary"]>50000] this is single condition
# filtered_Rows = df[(df["salary"]>50000) & (df["column2] < 80000)
# ] we can replace salary with column and 50000 with value

# selecting columns
# 1a series
# 2. dataframe multiple columns of data
# column = df("Column name") for secific column
# subset = df("column1","column2","....) for multiple columns



# combine multiple condition

import pandas as pd


data = {
    "Name":['aqsa','ali', 'lily'],
    "age":[10,20,30],
    "city":['lahore','karachi','islamabad']
}

df = pd.DataFrame(data)
print(df)
print(f"Shape: {df.shape}")
print(f"Column: {df.columns}")