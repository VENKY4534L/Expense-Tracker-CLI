# 📊 Expense Tracker CLI

A Command-Line Expense Tracker built using Python to manage income and expenses efficiently.
This application allows users to record transactions, store them persistently, generate monthly summaries, export reports, and optionally create visual charts.

## 🚀 Features

Add income and expense entries via CLI

Store data persistently using CSV

Automatic date handling

Generate monthly summaries (income, expense, balance)

Export data to CSV and Excel

Optional chart export using matplotlib

Simple and lightweight CLI-based tool

## 🛠 Technologies Used

Python 3

CSV File Handling

Pandas

Matplotlib

Argparse (CLI handling)

OpenPyXL (Excel export)

~~~ 📁 Project Structure
expense_tracker/
│
├── expense_tracker.py
├── expenses.csv
├── export.csv
├── export.xlsx
├── summary.png
└── README.md
~~~
## ⚙️ Installation
### 1️⃣ Clone the Repository
git clone https://github.com/your-username/expense-tracker-cli.git
cd expense-tracker-cli

### 2️⃣ Install Dependencies
pip install pandas matplotlib openpyxl

### ▶️ Usage
➕ Add Income or Expense
python expense_tracker.py add income Salary 25000 --date 2025-01-05
python expense_tracker.py add expense Food 500
python expense_tracker.py add expense Travel 1200

### 📅 View Monthly Summary
python expense_tracker.py summary 1 2025

### 📤 Export Data
python expense_tracker.py summary 1 2025 --export

### 📈 Generate Chart
python expense_tracker.py summary 1 2025 --chart

## 📊 Sample Output
Summary for 1/2025
Income : 25000
Expense: 1700
Balance: 23300

## 🧠 Concepts Demonstrated

File Input/Output (CSV)

Date parsing and filtering

Data aggregation and grouping

Command-line argument handling

Report exporting

Data visualization

## 📌 Future Enhancements

SQLite database support

Category-wise expense analytics

Interactive menu-based UI

Password-protected user accounts

Cloud-based storage integration

## 👤 Author

Venkatesh Chintada
Computer Science & Engineering Student

GitHub: https://github.com/VENKY4534L

LinkedIn: https://www.linkedin.com/in/venkatesh-chintada-aab10625a/

## 📄 License

This project is licensed for educational and personal use.
