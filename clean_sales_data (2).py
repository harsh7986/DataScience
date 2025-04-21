import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# ============================
# 1. Initial Checks
# ============================
print("Initial dataset info:\n")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# ============================
# 2. Drop Duplicates
# ============================
# df = df.drop_duplicates()

# ============================
# 3. Remove rows with all NaNs
# ============================
df = df.dropna(how='all')

# ============================
# 4. Remove rows with missing critical values
# ============================
required_columns = ['date', 'store', 'item', 'sales']
df = df.dropna(subset=required_columns)

# ============================
# 5. Convert Data Types
# ============================
df = df[df['date'].astype(str).str[0:2] != 'da']  # Removes bad header rows if any

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

df = df.dropna(subset=['sales', 'date'])

# ============================
# 6. Feature Engineering
# ============================
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['year'] = df['date'].dt.year
df['weekday'] = df['date'].dt.day_name()


# ============================
# 7. Rename Columns
# ============================
df.columns = df.columns.str.lower().str.replace(' ', '_')

# ============================
# 8. Save Cleaned Data
# ============================
df.to_csv("cleaned_sales_data.csv", index=False)
print("\n✅ Cleaned sales data saved as 'cleaned_sales_data.csv'")

# ============================
# 9. Summary
# ============================
summary = {
    "final_shape": df.shape,
    "columns": list(df.columns),
    "missing_values": df.isnull().sum().to_dict(),
}

print("\n📋 Cleaning Summary:")
for k, v in summary.items():
    print(f"{k}: {v}")