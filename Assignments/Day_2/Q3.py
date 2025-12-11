# Q3: Given a CSV file Products.csv with columns:
# Write a Python program to:
# a) Read the CSV
# b) Print each row in a clean format
# c) Total number of rows
# d) Total number of products priced above 500
# e) Average price of all products
# f) List all products belonging to a specific category (user input)
# g) Total quantity of all items in stock

import pandas as pd

df=pd.read_csv("D:\Sunbeam_Internship_GenAI\GIT_Sunbeam\GenAI_94679_11-12-2025\GenAI_94679_11-12-2025\Assignments\Day_2\CSVs\products.csv")

print(df)
print("Total number of rows : ",len(df))
print("Total number of products priced above 500 : \n",df[df['price']>500])
print("Average price of all products : \n",df['price'].mean())
print("List all products belonging to a specific category (user input) : \n",df[df['category'] == 'Electronics'])
