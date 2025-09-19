# 💰 Expense Tracker

A simple Python expense tracker that allows you to input expenses, save them to a CSV file, and get expense summaries with budget tracking. 📊

## ✨ Features

- 📝 Input expense name, category, and amount.
- 💾 Save expenses to a CSV file (`file/expenses.csv`).
- 📊 Summarize expenses by category.
- 💸 Track total spending against a set budget.
- 📅 Calculate remaining budget and daily budget for the rest of the current month.

---

## ⚙️ Requirements

- Python 3.x
- `expense.py` module containing the `Expense` class. 📦

---

## 🚀 How to Use

1. **Run the script**:


2. You will be prompted to enter:

- 🏷️ Expense name
- 💵 Expense amount
- 📂 Select a category from a list (Food, Home, Work, Fun, Music)

3. The expense will be saved automatically to `file/expenses.csv`. 💾

4. The script will then display:

- 🧾 Total expenses by category
- 💰 Total amount spent
- 🎯 Remaining budget (default set to 700,000.00)
- 📆 Daily budget for the remaining days of the month

---

## 📂 File Structure

file/
└── expenses.csv # CSV file where expenses are stored 🗂️

expense.py # Module containing Expense class (required) 📦
expense_tracker.py # Main script (this script) 📝



---

## 🍽️ Expense Categories

- Food 🍔
- Home 🏠
- Work 💼
- Fun 🎉
- Music 🎵

---

## 💵 Budget

- The default budget is set to `$700,000.00`. You can change this in the script by modifying the `budget` variable in the `main()` function. 🔧

---

## 🛠️ Functions Overview

- `get_user_expense()`: Prompts user for expense details and returns an `Expense` object. 🤝
- `save_user_expense(expense, expense_file_path)`: Saves an expense to the CSV file. 💾
- `summarize_expenses(expense_file_path, budget)`: Reads all expenses, summarizes by category, and shows budget info. 📊
- `green_text(text)`: Returns the given text formatted to appear green in the terminal (used internally). 🟢

---

## ⚠️ Notes

- Make sure to create the `file/` directory before running the script. 🗂️
- The script appends new expenses to keep a full history. 📝
- Date and budget calculations are based on the current date and calendar month. 🕒

---

## 🎯 Example Output

Running Expense Tracker!
Getting user Expense
Enter the expense name: Coffee ☕
Enter the expense amount: 5.50
Select a category:
1, Food 🍔
2, Home 🏠
3, Work 💼
4, Fun 🎉
5, Music 🎵
Enter the category number [1 - 5]: 1
Saving user Expense: Coffee Food 5.5 file/expenses.csv
Summarizing User Expenses
Expenses By Category:
Food: $25.50
Home: $100.00
Total Spent: $125.50
Remaining Budget: $699874.50
Daily Budget for the remaining 12 days: $58322.88


---

Feel free to extend or customize this expense tracker as needed for your projects! 🚀
