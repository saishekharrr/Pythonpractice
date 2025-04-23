def main():
    print("Welcome to Expense Tracker ")
    expenses = []

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Goodbye! ")
            break
        else:
            print("Invalid choice. Try again.")

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g. food, travel, bills): ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added!")

def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    total = sum(item['amount'] for item in expenses)
    print(f"\n Total Spent: ₹{total}")
    print("Category-wise breakdown:")
    
    categories = {}
    for item in expenses:
        cat = item['category']
        categories[cat] = categories.get(cat, 0) + item['amount']
    
    for cat, amt in categories.items():
        print(f" - {cat}: ₹{amt}")

if __name__ == "__main__":
    main()