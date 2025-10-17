expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: $"))
    category = input("Enter expense category: ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print(f"✅ Added {name} (${amount}) to {category} category.\n")

def view_expense():
    if not expenses:
        print("You have not recorded any expenses yet.\n")
        return
    else:
        print("📋 Here are your expenses:")
        for expense in expenses:
            print(f"- {expense['name']}: ${expense['amount']} ({expense['category']})")
        print()

def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"💰 Total Amount Spent: ${total}\n")

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()