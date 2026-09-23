[README (3).md](https://github.com/user-attachments/files/32559176/README.3.md)
# adventure-expense_tracker#

A simple Python command-line tool that reads your transactions from a CSV file and generates a spending summary plus visual charts — income vs. expenses, spending by category, and your balance over time.

## Features

Console summary: total income, total expenses, net savings, and savings rate
- Pie chart of spending by category
- Bar chart comparing monthly income vs. expenses
-  Line chart showing your running balance over time
-  Includes a sample `transactions.csv` so it works immediately, no setup required

## Demo Output

Running the script prints a summary like this:

```
========================================
💰 PERSONAL FINANCE SUMMARY
========================================
Total Income:    $7,650.00
Total Expenses:  $3,624.44
Net Savings:     $4,025.56
Savings Rate:    52.6%
========================================

Top spending categories:
  Housing         $2,700.00
  Food            $509.45
  Bills           $180.00
  Transport       $90.00
  Entertainment   $105.99
  Health          $40.00
```

...and saves three chart images to the project folder.

## Installation

Clone the repo:

```bash
git clone https://github.com/YOUR-USERNAME/personal-finance-dashboard.git
cd personal-finance-dashboard
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the dashboard:

```bash
python finance_dashboard.py
```

If no `transactions.csv` file is found, the script automatically creates a sample one so you can see it in action right away.

To use your own data, replace `transactions.csv` with your own transactions using the same format:

| date       | description | category | amount  | type    |
|------------|-------------|----------|---------|---------|
| 2026-09-01 | Salary      | Income   | 3200.00 | income  |
| 2026-09-04 | Rent        | Housing  | -900.00 | expense |

**Column notes:**
- `date` — format `YYYY-MM-DD`
- `amount` — positive for income, negative for expenses
- `type` — must be exactly `income` or `expense`

## Output Files

After running, you'll find these in your project folder:

- `spending_by_category.png`
- `monthly_trend.png`
- `balance_over_time.png`

## Built With

- [pandas](https://pandas.pydata.org/) — data loading and aggregation
- [matplotlib](https://matplotlib.org/) — chart generation

## Possible Improvements

- [ ] Budget vs. actual comparison per category
- [ ] Support for multiple currencies
- [ ] Export summary as a PDF report
- [ ] Filter by custom date range

.
