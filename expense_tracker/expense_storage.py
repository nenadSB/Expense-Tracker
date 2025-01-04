import json
from pathlib import Path

# Path to the JSON file
EXPENSES_FILE = Path("expenses.json")

def load_expenses() -> list[dict]:
    """Load expenses from the JSON file."""
    if not EXPENSES_FILE.exists():
        return []  # Return an empty list if the file doesn't exist

    try:
        with EXPENSES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []  # Return an empty list if the file contains invalid JSON

def save_expenses(expenses: list[dict]) -> None:
    """Save expenses to the JSON file."""
    with EXPENSES_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def add_expense(date: str, amount: float, category: str) -> None:
    """Add a new expense to the JSON file."""
    expenses = load_expenses()
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category
    })
    save_expenses(expenses)