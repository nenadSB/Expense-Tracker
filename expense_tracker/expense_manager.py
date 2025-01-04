from datetime import datetime
from expense_storage import add_expense, load_expenses

def add_expense_interactive() -> None:
    """Add a new expense interactively."""
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category (e.g., Food, Transport): ")
    date = input("Enter the date (YYYY-MM-DD): ") or datetime.now().strftime("%Y-%m-%d")

    add_expense(date, amount, category)
    print("Expense added successfully!")

def view_expenses() -> None:
    """View all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nAll Expenses:")
        for expense in expenses:
            print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}")

def summarize_expenses() -> None:
    """Summarize expenses by category and month."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Summarize by category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nCategory-wise Summary:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

    # Summarize by month
    month_totals = {}
    for expense in expenses:
        month = expense["date"][:7]  # Extract YYYY-MM
        month_totals[month] = month_totals.get(month, 0) + expense["amount"]

    print("\nMonthly Summary:")
    for month, total in month_totals.items():
        print(f"{month}: ${total:.2f}")