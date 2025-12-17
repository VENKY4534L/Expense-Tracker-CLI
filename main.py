import csv
import os
from datetime import datetime
import argparse
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "type", "category", "amount"])

def add_entry(entry_type, category, amount, date):
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, entry_type, category, amount])
    print("Entry added successfully")

def monthly_summary(month, year):
    df = pd.read_csv(FILE_NAME)
    df["date"] = pd.to_datetime(df["date"])

    filtered = df[(df["date"].dt.month == month) & (df["date"].dt.year == year)]

    income = filtered[filtered["type"] == "income"]["amount"].sum()
    expense = filtered[filtered["type"] == "expense"]["amount"].sum()
    balance = income - expense

    print(f"\nSummary for {month}/{year}")
    print(f"Income : {income}")
    print(f"Expense: {expense}")
    print(f"Balance: {balance}")

    return filtered

def export_data(df):
    df.to_csv("export.csv", index=False)
    df.to_excel("export.xlsx", index=False)
    print("Data exported to export.csv and export.xlsx")

def generate_chart(df):
    summary = df.groupby("type")["amount"].sum()
    summary.plot(kind="bar")
    plt.title("Income vs Expense")
    plt.savefig("summary.png")
    plt.close()
    print("Chart saved as summary.png")

def main():
    init_file()

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("type", choices=["income", "expense"])
    add.add_argument("category")
    add.add_argument("amount", type=float)
    add.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))

    summary = subparsers.add_parser("summary")
    summary.add_argument("month", type=int)
    summary.add_argument("year", type=int)
    summary.add_argument("--export", action="store_true")
    summary.add_argument("--chart", action="store_true")

    args = parser.parse_args()

    if args.command == "add":
        add_entry(args.type, args.category, args.amount, args.date)

    elif args.command == "summary":
        df = monthly_summary(args.month, args.year)
        if args.export:
            export_data(df)
        if args.chart:
            generate_chart(df)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
