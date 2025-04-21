import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_sales_data.csv", parse_dates=["date"])

# Set visualization style
sns.set(style="whitegrid")

# ============================
# 1. Total Sales by Month
# ============================
monthly_sales = df.groupby(df['date'].dt.to_period("M"))["sales"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Month")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# ============================
# 2. Sales by Store
# ============================
store_sales = df.groupby("store")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=store_sales.index, y=store_sales.values, palette="coolwarm")
plt.title("Total Sales by Store")
plt.ylabel("Sales")
plt.xlabel("Store")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("store_sales.png")
plt.show()

# ============================
# 3. Sales by Item
# ============================
item_sales = df.groupby("item")["sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=item_sales.values, y=item_sales.index, palette="viridis")
plt.title("Top 10 Best-Selling Items")
plt.xlabel("Sales")
plt.ylabel("Item")
plt.tight_layout()
plt.savefig("top_items.png")
plt.show()

# ============================
# 4. Sales Trend Over Time
# ============================
daily_sales = df.groupby("date")["sales"].sum()

plt.figure(figsize=(14, 6))
sns.lineplot(x=daily_sales.index, y=daily_sales.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("daily_trend.png")
plt.show()
