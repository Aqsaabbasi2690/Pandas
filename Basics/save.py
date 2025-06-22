import pandas as pd

data = {
    "Name":['aqsa','ali', 'lily'],
    "age":[10,20,30],
    "city":['lahore','karachi','islamabad']
}

df = pd.DataFrame(data) #Dataframe is use to store data in a tabular format. Table with rows and columns
print(df)

# df.to_csv("data.csv",index=False)
  # Save DataFrame to CSV file

df.to_excel("data.xlsx",index=False) 
# df.to_json("data.json",index=False) 