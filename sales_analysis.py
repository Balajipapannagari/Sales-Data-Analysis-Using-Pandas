import pandas as pd

# Load datasets
sales_df = pd.read_csv("sales_data.csv")
cost_df = pd.read_csv("product_cost.csv")

# Convert Date column to datetime
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

# Create Month column
sales_df["Month"] = sales_df["Date"].dt.month_name()

# ------------------------------
# Monthly Revenue
# ------------------------------
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["Price"]

monthly_revenue = sales_df.groupby("Month")["Revenue"].sum()

print("\n Monthly Revenue:")
print(monthly_revenue)

# ------------------------------
# Top Selling Products
# ------------------------------
top_products = sales_df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\n Top Selling Products:")
print(top_products)

# ------------------------------
# Region-wise Sales
# ------------------------------
region_sales = sales_df.groupby("Region")["Revenue"].sum()

print("\n Region-wise Sales:")
print(region_sales)

# ------------------------------
# Profit Calculation
# ------------------------------
merged_df = pd.merge(sales_df, cost_df, on="Product")

def calculate_profit(row):
    return (row["Price"] - row["CostPrice"]) * row["Quantity"]

merged_df["Profit"] = merged_df.apply(calculate_profit, axis=1)

total_profit = merged_df["Profit"].sum()

print("\n Total Profit:", total_profit)
