import pandas as pd


data = {
    "Name":['aqsa','ali', 'lily'],
    "Age":[10,20,30],
    "City":['lahore','karachi','islamabad'],
    "Salary" : [10000 , 20000 , 30000 ]
}

df = pd.DataFrame(data)
print("Displaying the describe of data set")
print(df)
print("descriptive statistics of the data set")
print(df.describe())


# The describe() method in pandas provides a summary of the statistics of the DataFrame.


