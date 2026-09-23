"""
Python Project: Personal Finance Dashboard
--------------------------------------------------
What this teaches you:
- Reading data from a CSV file (with pandas)
- Filtering and grouping data
- Generating charts (with matplotlib)
- Working with dates
- Writing a clean summary report to the console

Setup (run once in your terminal):
    pip install pandas matplotlib

How to run:
    python finance_dashboard.py

It reads 'transactions.csv' (in the same folder) and:
  1. Prints a summary to the console (income, expenses, savings)
  2. Saves 3 chart images: spending_by_category.png,
     monthly_trend.png, and balance_over_time.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_FILE = "transactions.csv"


# ---- 1. Load and prepare data ----

def load_data():
    """Load transactions from CSV and prepare the columns we need."""
    if not os.path.exists(DATA_FILE):
        print(f"⚠️  '{DATA_FILE}' not found. Creating a sample file for you...")
        create_sample_csv()

    df = pd.read_csv(DATA_FILE)

    # Make sure date column is treated as an actual date, not text
    df["date"] = pd.to_datetime(df["date"])

    # Add a "month" column (e.g. "2026-08") — useful for grouping later
    df["month"] = df["date"].dt.to_period("M").astype(str)

    return df


def create_sample_csv():
    """Generate a small sample transactions file so the dashboard works out of the box."""
    sample_data = """date,description,category,amount,type
2026-07-02,Salary,Income,3200.00,income
2026-07-03,Rent,Housing,-900.00,expense
2026-07-05,Groceries,Food,-120.50,expense
2026-07-08,Netflix,Entertainment,-15.99,expense
2026-07-10,Uber,Transport,-32.00,expense
2026-07-15,Freelance Gig,Income,450.00,income
2026-07-18,Restaurant,Food,-65.00,expense
2026-07-20,Electricity Bill,Bills,-80.00,expense
2026-08-01,Salary,Income,3200.00,income
2026-08-03,Rent,Housing,-900.00,expense
2026-08-06,Groceries,Food,-140.20,expense
2026-08-09,Gym Membership,Health,-40.00,expense
2026-08-12,Uber,Transport,-28.00,expense
2026-08-15,Freelance Gig,Income,300.00,income
2026-08-19,Phone Bill,Bills,-45.00,expense
2026-08-22,Concert Tickets,Entertainment,-90.00,expense
2026-09-01,Salary,Income,3200.00,income
2026-09-04,Rent,Housing,-900.00,expense
2026-09-07,Groceries,Food,-135.75,expense
2026-09-11,Uber,Transport,-30.00,expense
2026-09-14,Freelance Gig,Income,500.00,income
2026-09-17,Internet Bill,Bills,-55.00,expense
2026-09-20,Dinner Out,Food,-48.00,expense
"""
    with open(DATA_FILE, "w") as f:
        f.write(sample_data)


# ---- 2. Console summary ----

def print_summary(df):
    """Print an overview of income, expenses, and savings."""
    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expenses = df[df["type"] == "expense"]["amount"].sum()  # negative number
    net_savings = total_income + total_expenses

    savings_rate = (net_savings / total_income * 100) if total_income > 0 else 0

    print("=" * 40)
    print("💰 PERSONAL FINANCE SUMMARY")
    print("=" * 40)
    print(f"Total Income:    ${total_income:,.2f}")
    print(f"Total Expenses:  ${abs(total_expenses):,.2f}")
    print(f"Net Savings:     ${net_savings:,.2f}")
    print(f"Savings Rate:    {savings_rate:.1f}%")
    print("=" * 40)

    print("\nTop spending categories:")
    category_totals = (
        df[df["type"] == "expense"]
        .groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )
    for cat, amount in category_totals.items():
        print(f"  {cat:<15} ${amount:,.2f}")


# ---- 3. Charts ----

def chart_spending_by_category(df):
    """Pie chart showing what percentage of spending went to each category."""
    expenses = df[df["type"] == "expense"]
    category_totals = expenses.groupby("category")["amount"].sum().abs()

    plt.figure(figsize=(7, 7))
    plt.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=90)
    plt.title("Spending by Category")
    plt.tight_layout()
    plt.savefig("spending_by_category.png")
    plt.close()
    print("📊 Saved: spending_by_category.png")


def chart_monthly_trend(df):
    """Bar chart comparing income vs. expenses per month."""
    monthly = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)

    if "expense" in monthly.columns:
        monthly["expense"] = monthly["expense"].abs()

    monthly.plot(kind="bar", figsize=(8, 5))
    plt.title("Monthly Income vs. Expenses")
    plt.ylabel("Amount ($)")
    plt.xlabel("Month")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("monthly_trend.png")
    plt.close()
    print("📊 Saved: monthly_trend.png")


def chart_balance_over_time(df):
    """Line chart showing cumulative balance over time."""
    df_sorted = df.sort_values("date").copy()
    df_sorted["running_balance"] = df_sorted["amount"].cumsum()

    plt.figure(figsize=(8, 5))
    plt.plot(df_sorted["date"], df_sorted["running_balance"], marker="o")
    plt.title("Balance Over Time")
    plt.ylabel("Balance ($)")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("balance_over_time.png")
    plt.close()
    print("📊 Saved: balance_over_time.png")


# ---- 4. Main ----

def main():
    df = load_data()
    print_summary(df)

    print("\nGenerating charts...")
    chart_spending_by_category(df)
    chart_monthly_trend(df)
    chart_balance_over_time(df)

    print("\n✅ Done! Open the .png files to view your charts.")


if __name__ == "__main__":
    main()
