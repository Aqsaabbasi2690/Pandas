import pandas as pd


data = {
    "Name":['aqsa','ali', 'lily', 'john'],
    "age":[10,20,30,40],
    "city":['lahore','karachi','islamabad', 'multan'],
    "Salary":[100000,20000,50000,60000]
}

df = pd.DataFrame(data)
print("Displaying Sample DataFrame")
print(df)
#single column
print("Names (Single column return series)")
print(df["Name"])

#multiple columns
subset = df[["Name", "age"]]
print("Subset of DataFrame with multiple columns")
print(subset)


#selecting  single rows
high_salary = df[df["Salary"] > 50000]
print("Selecting a single row emoployees with salary greater than 50000")
print(high_salary)


#selecting multiple rows, employees with age greater than 30 & salary less than 50000
high_age = df[(df["age"] > 30) & (df["Salary"] < 50000)]
print("Selecting multiple rows employees with age greater than 30 and salary less than 50000")
print(high_age)


# using or  condition, employees with age greater than 30 or salary less than 50000
high_age_or_salary = df[(df["age"] > 30) | (df["Salary"] < 50000)]
print("Using OR condition, employees with age greater than 30 or salary less than 50000")
print(high_age_or_salary)