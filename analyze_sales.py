import pandas as pd

# 1. Load the dataset
df = pd.read_csv("ecommerce_sales.csv")

# 2. Data Engineering: Calculate Total Revenue for each transaction
# Revenue = Quantity * Price Per Unit
df['Total_Revenue'] = df['Quantity'] * df['Price_Per_Unit']

print("--- Business Analytics Summary ---\n")

# Insight 1: Calculate overall store metrics
total_sales_value = df['Total_Revenue'].sum()
total_items_sold = df['Quantity'].sum()
print(f"Total Store Revenue: ${total_sales_value:,.2f}")
print(f"Total Units Sold: {total_items_sold:,} items")
print("-" * 50)

# Insight 2: Total Revenue breakdown per Product Category
print("\n--- Revenue Breakdown per Product Category ---")
category_revenue = df.groupby("Product_Category")['Total_Revenue'].sum().sort_values(ascending=False)
print(category_revenue.map('${:,.2f}'.format))
print("-" * 50)

# Insight 3: Preferred payment methods by customers
print("\n--- Most Popular Payment Methods ---")
payment_counts = df['Payment_Method'].value_counts()
print(payment_counts)
print("-" * 50)

# Insight 4: Average customer age per product department
print("\n--- Average Customer Age per Category ---")
category_age = df.groupby("Product_Category")['Customer_Age'].mean().round(1)
print(category_age)
