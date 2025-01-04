from expense_manager import add_expense_interactive, view_expenses, summarize_expenses
from data_visualizer import visualize_expenses

def main() -> None:
    """Main menu for the Expense Tracker."""
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Visualize Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense_interactive()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            visualize_expenses()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()