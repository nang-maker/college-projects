import json


# Load saved expenses from the JSON file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save expenses to the JSON file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense():
    print("\n===== Add Expense =====")

    # Ask for the expense category
    while True:
        category = input("Category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # Ask for the amount and make sure it is valid
    while True:
        try:
            amount = float(input("Amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Ask for a description
    while True:
        description = input("Description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    # Store the expense as a dictionary
    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    # Add the expense to the list
    expenses.append(expense)

    # Save the updated expenses
    save_expenses()

    print("Expense added successfully!")


# Display all recorded expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n===== Your Expenses =====")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['category']} - "
            f"${expense['amount']:.2f} - "
            f"{expense['description']}"
        )


# Display the total expenses
def show_total():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: ${total:.2f}")


# Display spending by category
def show_categories():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n===== Category Summary =====")

    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")


# Delete an expense
def delete_expense():
    if not expenses:
        print("\nNo expenses to delete.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)

        save_expenses()

        print(
            f"Deleted: {removed['category']} - "
            f"${removed['amount']:.2f}"
        )

    except ValueError:
        print("Please enter a valid number.")


# Load saved expenses when the program starts
expenses = load_expenses()


# Main menu
while True:
    print("\n================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Category Summary")
    print("5. Delete Expense")
    print("6. Exit")
    print("================================")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        show_categories()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")