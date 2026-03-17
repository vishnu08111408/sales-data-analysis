import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Display data
print("Dataset:\n", data)

# Data cleaning
data.dropna(inplace=True)

# Total sales by category
category_sales = data.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)

# Total sales by region
region_sales = data.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

# Plot category sales
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Plot region sales
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()