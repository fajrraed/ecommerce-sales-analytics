import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Fix random seed for exact generation replication
np.random.seed(101)

records = 1500
start_date = datetime(2026, 1, 1)

# Generate baseline transactional elements
tx_ids = [f"TXN_{1000 + i}" for i in range(records)]
cust_ids = [f"CUST_{np.random.randint(100, 500)}" for _ in range(records)]
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Beauty"]
chosen_categories = np.random.choice(categories, size=records, p=[0.3, 0.25, 0.2, 0.15, 0.1])

# Generate realistic quantity distributions based on category
quantities = np.random.choice([1, 2, 3, 4, 5], size=records, p=[0.4, 0.3, 0.15, 0.1, 0.05])
payment_methods = np.random.choice(["Credit Card", "PayPal", "Crypto", "Debit Card"], size=records)
ages = np.random.randint(18, 70, size=records)
dates = [start_date + timedelta(days=int(np.random.randint(0, 300))) for _ in range(records)]

# Create variation in item pricing based on specific categories
prices = []
for cat in chosen_categories:
    if cat == "Electronics": prices.append(np.round(np.random.uniform(150, 1200), 2))
    elif cat == "Clothing": prices.append(np.round(np.random.uniform(15, 150), 2))
    elif cat == "Home & Kitchen": prices.append(np.round(np.random.uniform(20, 400), 2))
    elif cat == "Books": prices.append(np.round(np.random.uniform(10, 60), 2))
    else: prices.append(np.round(np.random.uniform(10, 120), 2))

# Compile dataset into structured frame
df = pd.DataFrame({
    "Transaction_ID": tx_ids,
    "Customer_ID": cust_ids,
    "Product_Category": chosen_categories,
    "Quantity": quantities,
    "Price_Per_Unit": prices,
    "Payment_Method": payment_methods,
    "Purchase_Date": [d.strftime("%Y-%m-%d") for d in dates],
    "Customer_Age": ages
})

# Save output to project environment
df.to_csv("ecommerce_sales.csv", index=False)
print("Dataset 'ecommerce_sales.csv' successfully created with 1500 checkout records.")
