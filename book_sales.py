# -*- coding: utf-8 -*-
"""Book_Sales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r1ISjJoa3H0hOYb9B2jVQvwLlkq1WzTo
"""

# Import the pandas library
import pandas as pd

# Load the dataset
df = pd.read_excel("Book_Sales.xlsx")

#Explore the dataset
df.head()

# Check for duplicates
print("Checking for duplicates...")
duplicates = df.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")

# Step 2: Check for data types
df.dtypes

# Step 3: Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

#get summary statistics for the DataFrame
df.describe()

# number of books per genre
df.groupby("Genre")["Name"].count()

# average rating per genre
df.groupby("Genre")["User Rating"].mean()

# books per year
df.groupby("Year")["Name"].count()

# books with more than 10, 000 reviews
df[df["Reviews"] >= 10000]

# Sort by Books into top 10 highest user rating order
sorted_df = df.sort_values("User Rating", ascending =False)
sorted_df[["Name", "User Rating"]].head(10)

# Sort by Books into top 10 highest price order
sorted_df = df.sort_values("Price", ascending =False)
sorted_df[["Name", "Price"]].head(10)

#Visulaisation
import matplotlib.pyplot as plt
import seaborn as sns

#histogram
df[["User Rating", "Reviews"]].hist(figsize=(7,5))

plt.show()

#histogram using bins
df[["Price"]].hist(bins=5, figsize=(7,5))
plt.show()

#max and min reviews
df["Reviews"].agg(["min","max"])

#Correlation Heatmap
df[["Reviews", "User Rating"]].corr()

corr = df[["Reviews","User Rating"]].corr()

plt.figure(figsize=(9,6))
sns.heatmap(corr)

plt.show()

#bar plot
sns.barplot(x="Genre", y="Price", data=df, errorbar=None)

plt.show()