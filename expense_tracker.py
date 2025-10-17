# expense_tracker.py

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: $"))
    category = input("Enter category: ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print(f"✅ Added {name} (${amount}) to {category} category.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("📋 All Expenses:")
    for e in expenses:
        print(f"- {e['name']}: ${e['amount']} ({e['category']})")
    print()

def total_expenses():
    total = sum(e['amount'] for e in expenses)
    print(f"💰 Total Spent: ${total}\n")

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
