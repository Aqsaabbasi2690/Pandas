import pandas as pd

# Create the sample data (run this once to generate the Excel file)
data = {
    'ORDERNUMBER': [10107, 10121, 10134, 10145, 10159, 10350, 10373, 10386, 10168],
    'QUANTITYORDERED': [30, 34, 41, 45, 49, 20, 29, 43, 36],
    'PRICEEACH': [95.70, 81.35, 94.74, 83.26, 100.00, 100.00, 100.00, 100.00, 96.66],
    'ORDERLINENUMBER': [2, 5, 2, 6, 14, 15, 1, 4, 1],
    'TERRITORY': ['NA', 'EMEA', 'EMEA', 'NA', 'EMEA', 'EMEA', 'EMEA', 'EMEA', 'NA'],
    'CONTACTLASTNAME': ['Yu', 'Henriot', 'Da Cunha', 'Young', 'Brown', 'Freyre', 'Koskitalo', 'Freyre', 'Hirano'],
    'CONTACTFIRSTNAME': ['Kwai', 'Paul', 'Daniel', 'Julie', 'Julie', 'Diego', 'Pirkko', 'Diego', 'Juri'],
    'DEALSIZE': ['Small', 'Small', 'Medium', 'Medium', 'Medium', 'Small', 'Medium', 'Medium', 'Medium'],
    'SALES': [2871.00, 2765.90, 3884.34, 3746.70, 4900.00, 2000.00, 2900.00, 4300.00, 3479.76],
    'CUSTOMERNAME': ['Land of Toys Inc.', 'Reims Collectables', 'Motor Mint Distributors Inc.', 'Land of Toys Inc.', 'Corporate Gift Ideas Co.', 'Euro+ Shopping Channel', 'Royale Belge', 'Technics Stores Inc.', 'Technics Stores Inc.']
}

df = pd.DataFrame(data)
df.to_excel('SampleSuperstore.xlsx', index=False)
print("✅ Excel file created successfully!")