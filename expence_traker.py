class ExpenseTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount
        print("Income added")

    def add_expense(self, category, amount):
        self.expenses.append((category, amount))
        print("Expense added")

    def report(self):
        total_expense = sum(amount for _, amount in self.expenses)
        balance = self.income - total_expense

        print("\n--- REPORT ---")
        print("Income:", self.income)
        print("Expense:", total_expense)
        print("Balance:", balance)


tracker = ExpenseTracker()

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        tracker.add_income(amount)

    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        tracker.add_expense(category, amount)

    elif choice == "3":
        tracker.report()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
