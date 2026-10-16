import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set visual style for plots
sns.set_theme(style='whitegrid')

print('--- STEP 1: Generating Simulated Coffee Chain Dataset ---')
np.random.seed(42)
n_rows = 2000

dates = pd.date_range(start='2025-01-01', end='2025-12-31', periods=n_rows)
products = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']
regions = ['North America', 'Europe', 'Asia-Pacific']

data = {
    'Transaction_ID': range(10001, 10001 + n_rows),
    'Date': np.random.choice(dates, n_rows),
    'Product': np.random.choice(products, n_rows),
    'Region': np.random.choice(regions, n_rows),
    'Quantity': np.random.randint(1, 6, n_rows),
}

df = pd.DataFrame(data)

# Define pricing and cost mapping dictionaries
price_map = {
    'Espresso': 3.00,
    'Latte': 4.50,
    'Cappuccino': 4.00,
    'Americano': 3.50,
    'Mocha': 5.00,
}
cost_map = {
    'Espresso': 0.80,
    'Latte': 1.50,
    'Cappuccino': 1.20,
    'Americano': 0.90,
    'Mocha': 1.80,
}

df['Unit_Price'] = df['Product'].map(price_map)
df['Unit_Cost'] = df['Product'].map(cost_map)

print(df.head())

print('\n--- STEP 2: Data Cleaning & Feature Engineering ---')
# Check for null values
print('Null values found:', df.isnull().sum().sum())

# Ensure proper data types & extract time features
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Day_Of_Week'] = df['Date'].dt.day_name()

# Calculate financial metrics
df['Total_Revenue'] = df['Quantity'] * df['Unit_Price']
df['Total_Cost'] = df['Quantity'] * df['Unit_Cost']
df['Total_Profit'] = df['Total_Revenue'] - df['Total_Cost']
df['Profit_Margin'] = (df['Total_Profit'] / df['Total_Revenue']) * 100

# Executive Summary Metrics
total_rev = df['Total_Revenue'].sum()
total_cost = df['Total_Cost'].sum()
total_profit = df['Total_Profit'].sum()
avg_margin = df['Profit_Margin'].mean()

print('========================================')
print(f'TOTAL REVENUE:  ${total_rev:,.2f}')
print(f'TOTAL COST:     ${total_cost:,.2f}')
print(f'TOTAL PROFIT:   ${total_profit:,.2f}')
print(f'AVERAGE MARGIN: {avg_margin:.2f}%')
print('========================================')

print('\n--- STEP 3: Aggregating Product & Regional Insights ---')
product_summary = (
    df.groupby('Product')
    .agg(
        {
            'Quantity': 'sum',
            'Total_Revenue': 'sum',
            'Total_Profit': 'sum',
            'Profit_Margin': 'mean',
        }
    )
    .sort_values(by='Total_Profit', ascending=False)
    .reset_index()
)

print('\nProduct Performance Summary:')
print(product_summary)

region_summary = (
    df.groupby('Region')
    .agg(
        {
            'Total_Revenue': 'sum',
            'Total_Profit': 'sum',
            'Profit_Margin': 'mean',
        }
    )
    .sort_values(by='Total_Profit', ascending=False)
    .reset_index()
)

print('\nRegional Performance Summary:')
print(region_summary)

print('\n--- STEP 4: Visualizing Results ---')
print('Generating visual charts... Close the chart window to finish execution.')

plt.figure(figsize=(14, 6))

# Plot 1: Total Profit by Product
plt.subplot(1, 2, 1)
sns.barplot(
    data=product_summary, x='Product', y='Total_Profit', palette='viridis'
)
plt.title('Total Profit by Product Category')
plt.xlabel('Product')
plt.ylabel('Total Profit ($)')

# Plot 2: Regional Revenue Comparison
plt.subplot(1, 2, 2)
sns.barplot(
    data=region_summary, x='Region', y='Total_Revenue', palette='magma'
)
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue ($)')

plt.tight_layout()
# save the chart as an image before showing it
plt.savefig('coffee_sales_analysis.png', dpi=300, bbox_inches='tight')
print('chart successfully saved as coffee_sales_analysis.png!')

plt.show()

# --- STEP 5: Time-Series Monthly Revenue Trend ---
monthly_trend = (
    df.groupby(df['Date'].dt.to_period('M'))['Total_Revenue']
    .sum()
    .reset_index()
)
monthly_trend['Date'] = monthly_trend['Date'].dt.to_timestamp()

print('\n--- Monthly Revenue Trend ---')
print(monthly_trend)

# Plotting the monthly trend line charts
plt.figure(figsize=(12, 5))
sns.lineplot(
    data=monthly_trend,
    x='Date',
    y='Total_Revenue',
    marker='o',
    color='saddlebrown',
    linewidth=2.5,
)
plt.title('Coffee Chain Monthly Revenue Trend (2025)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the trend chart as well
plt.savefig('monthly_revenue_trend.png', dpi=300, bbox_inches='tight')
plt.show()

# --- STEP 5: Exporting Data Reports to CSV ---
# This saves your aggregated product and region summaries directly into your folder
product_summary.to_csv('product_performance_summary.csv', index=False)
region_summary.to_csv('region_performance_summary.csv', index=False)
print(
    '\nReports successfully exported as CSV files (product_performance_summary.csv & region_performance_summary.csv)!'
)


# --- STEP 6: Correlation Analysis & Heatmap ---
# Let's see how numerical variables correlate with each other
plt.figure(figsize=(8, 6))

# Select only numerical columns for correlation
numerical_df = df[
    [
        'Quantity',
        'Unit_Price',
        'Unit_Cost',
        'Total_Revenue',
        'Total_Cost',
        'Total_Profit',
        'Profit_Margin',
    ]
]
correlation_matrix = numerical_df.corr()

# Draw the heatmap
sns.heatmap(
    correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5
)
plt.title('Correlation Matrix of Coffee Chain Metrics', fontsize=14)
plt.tight_layout()

# Save correlation heatmap
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print('Correlation heatmap saved as correlation_heatmap.png!')

plt.show()

print(
    '\n🎉 Congratulations! Your Coffee Chain Sales & Profitability Analysis Project is fully complete!'
)