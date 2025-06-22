import pandas as pd

# why we need to understand data
# how many rowa and colums in our data?
# what type of data every rows and colums store like numbers,text,dates etc
# missing data we also dont know

# we solve all these by summarizing data for this purpose we use info method 
# 1. it display numbers of rows and column
# 2.column name
# 3.data type like int,float etc, non null also counts
# 4.memory usage of dataframe


data = {
    "Name":['aqsa','ali', 'lily'],
    "age":[10,20,30],
    "city":['lahore','karachi','islamabad']
}

df = pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info())