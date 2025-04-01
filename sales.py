" import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create the dataset
data = {
    "Product_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Sales": [10000, 52500, 35000, 45800, 38500, 65500, 105600, 89000, 13000, 40000, 110000, 5800],
    "Profit": [2500, 15000, 5000, 25000, 8500, 29500, 42600, 20000, 3000, 4000, 56000, 2500]
}

# Convert to a pandas DataFrame 
df = pd.DataFrame(data)

# Save as CSV file
df.to_csv("sales_data.csv", index=False)

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Display the first 10 rows
print(df.head(10))

# Calculate average sales and profit
average_sales = df["Sales"].mean()
average_profit = df["Profit"].mean()

print(f"Average Sales: {average_sales}")
print(f"Average Profit: {average_profit}")

# Line plot for sales trend
sns.set_style("whitegrid")
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["Month"], y=df["Sales"], marker="o", color="b")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

# Bar plot for profit 
plt.figure(figsize=(10, 5))
sns.barplot(x=df["Month"], y=df["Profit"], palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit")
plt.show()
 