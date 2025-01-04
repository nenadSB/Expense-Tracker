import matplotlib.pyplot as plt
from expense_storage import load_expenses

def visualize_expenses() -> None:
    """Visualize expenses using a pie chart."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Group expenses by category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    # Create a pie chart
    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Category-wise Spending")
    plt.show()