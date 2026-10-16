# ☕ Coffee Chain Sales & Profitability Analysis

An end-to-end data analysis project built in Python to evaluate multi-region coffee chain transactions, analyze product/regional profitability, track monthly revenue trends and generate automated executive reports.

---

## 📊 Project Overview
This project simulates and processes a 2,000-row transaction dataset for an international coffee chain. It performs data cleaning, feature engineering (calculating revenues, costs, margins and temporal trends), exploratory data analysis (EDA), and generates visual analytics using Python data science libraries.

---

## 🚀 Key Features & Workflow
1. Dataset Simulation: Generates multi-region transaction data with items, quantities, pricing and unit costs.
2. Data Cleaning & Feature Engineering: Extracts dates, months, days of the week and calculates total revenue, total cost, net profit, and profit margins.
3. Business Aggregations: Analyzes high-performing products and regional revenue/profit performance.
4. Data Visualization: Uses Matplotlib and Seaborn to plot product profits, regional revenues, monthly revenue trends and correlation heatmaps.
5. Automated Exporting: Exports processed summary reports to CSV files and saves high-resolution charts as image files.

---

## 🛠️ Technologies Used
* **Python 3.x**
* **Pandas** (Data manipulation & aggregation)
* **NumPy** (Numerical operations & data generation)
* **Matplotlib & Seaborn** (Data visualization & heatmaps)

---

## 📁 Project Structure
```text
Coffee_Sales_Project/
│
├── analysis.py                     # Main Python execution script
├── coffee_sales_analysis.png       # Bar chart: Product Profit vs Regional Revenue
├── monthly_revenue_trend.png       # Line chart: 2025 Monthly Revenue Trend
├── correlation_heatmap.png         # Heatmap: Numerical variables correlation
├── product_performance_summary.csv # Exported product summary table
└── region_performance_summary.csv  # Exported regional summary table
```

## ⚙️ How to Run the Project
Clone or Download this repository.

Open your terminal or command prompt and install the required libraries:

Bash
pip install pandas numpy matplotlib seaborn
Open the folder in VS Code or your preferred Python IDE.

Run the script:

Bash
python analysis.py

## 📈 Key Insights & Results
Top Product: The Mocha category generated the highest absolute profit, followed closely by Lattes.

Regional Distribution: North America led slightly in total revenue, maintaining close competition with Europe and Asia-Pacific markets.

Profitability: Maintaining tight control over unit costs on high-volume items like Americanos and Lattes significantly drove overall net margin health.

## 💡 Future Enhancements
Integrating a machine learning model (e.g., Scikit-Learn / Statsmodels) for future sales forecasting.
Building an interactive dashboard using Streamlit or Tableau.