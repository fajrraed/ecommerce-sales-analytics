import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data and calculate transaction revenue
df = pd.read_csv("ecommerce_sales.csv")
df['Total_Revenue'] = df['Quantity'] * df['Price_Per_Unit']

# Set clean aesthetic style for the plots
sns.set_theme(style="whitegrid")

# 2. Initialize a clear window layout for our visualizations
plt.figure(figsize=(12, 5))

# Plot 1: Horizontal Bar Chart showing Revenue per Product Category
plt.subplot(1, 2, 1)
category_data = df.groupby("Product_Category")['Total_Revenue'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=category_data, x='Total_Revenue', y='Product_Category', hue='Product_Category', legend=False, palette="viridis")
plt.title("Revenue by Product Category")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Category")

# Plot 2: Vertical Bar Chart showing Payment Method Usage Counts
plt.subplot(1, 2, 2)
payment_counts = df['Payment_Method'].value_counts().reset_index()
sns.barplot(data=payment_counts, x='Payment_Method', y='count', hue='Payment_Method', legend=False, palette="magma")
plt.title("Popularity of Payment Methods")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")

# Adjust spacing and display the window
plt.tight_layout()
plt.show()
