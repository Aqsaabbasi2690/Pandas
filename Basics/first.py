# Importing Pandas and Reading a CSV File from dataframe
# To use Pandas, you first need to import it and then read a CSV file into
import pandas as pd 
# df = pd.read_csv("C:\\Users\\Home\\OneDrive\\Desktop\\pandas\\sales_data_sample.csv", encoding="latin1")
# encoding is used to handle special characters in the CSV file

# print(df.head())


# Reading an Excel file

df = pd.read_excel("SampleSuperstore.xlsx", engine='openpyxl')
print("📊 Data loaded successfully!")

# Basic Data Exploration
print("\n1. First 5 rows:")
print(df.head())

print("\n2. Data Info:")
print(df.info())

print("\n3. Data Shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n4. Column Names:")
print(list(df.columns))

print("\n5. Deal Size Distribution:")
print(df['DEALSIZE'].value_counts())

print("\n6. Territory Analysis:")
print(df['TERRITORY'].value_counts())

print("\n7. Sales Statistics:")
print(f"Total Sales: ${df['SALES'].sum():,.2f}")
print(f"Average Sales: ${df['SALES'].mean():.2f}")

print("\n8. Top 5 Customers by Sales:")
top_customers = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head()
print(top_customers)