# Personal Expense Tracker

A simple command-line Personal Expense Tracker built with Python. This project allows users to record, view, summarize, and delete their daily expenses while automatically saving the data to a JSON file.

The project was created as a beginner-friendly Python application to practice fundamental programming concepts such as functions, lists, dictionaries, loops, conditional statements, exception handling, file handling, and JSON data storage.

---

## 📌 Project Overview

Managing daily expenses can be difficult when spending is recorded randomly or not recorded at all. The Personal Expense Tracker provides a simple way to keep track of expenses directly from the command line.

Users can:

* Add new expenses
* View all recorded expenses
* Calculate total spending
* View spending by category
* Delete individual expenses
* Automatically save expense data
* Load previously saved expenses when the program starts

The application uses a JSON file to store the expense data, meaning the information remains available even after the program is closed.

---

## 🎯 Project Goals

The main goal of this project is to build a practical Python application while developing a stronger understanding of programming fundamentals.

Through this project, I practiced:

* Variables and data types
* Lists
* Dictionaries
* Functions
* `if`, `elif`, and `else` statements
* `for` and `while` loops
* User input
* String formatting
* Error handling with `try` and `except`
* Reading and writing files
* JSON data
* Basic CRUD operations
* Organizing code into reusable functions

---

## ✨ Features

### 1. Add Expense

Users can enter:

* Expense category
* Amount
* Description

For example:

```text
Category: Food
Amount: 5.50
Description: Lunch
```

The expense is stored as a dictionary and added to the main expense list.

---

### 2. View Expenses

The program displays all recorded expenses with a numbered list.

Example:

```text
===== Your Expenses =====
1. Food - $5.50 - Lunch
2. Transport - $2.00 - Bus fare
3. Education - $10.00 - Study materials
```

Numbering makes it easier for users to identify an expense when they want to delete it.

---

### 3. Show Total

The application calculates the total amount of all recorded expenses.

Example:

```text
Total Expenses: $17.50
```

The program loops through the expense list and adds each amount together.

---

### 4. Category Summary

Expenses can be grouped by category to show how much money has been spent in each area.

Example:

```text
===== Category Summary =====
Food: $12.50
Transport: $5.00
Education: $10.00
```

This helps users understand where most of their money is going.

---

### 5. Delete Expense

Users can delete an expense by entering its number.

Example:

```text
Enter expense number to delete: 2

Deleted: Transport - $5.00
```

The selected item is removed from the list and the updated data is saved.

---

### 6. Automatic Data Storage

The application uses Python's built-in `json` module to save expenses to:

```text
expenses.json
```

When the program starts, it checks whether the file exists. If saved data is found, the application loads it automatically.

This means users do not lose their expenses when they close the program.

---

### 7. Input Validation

The application includes basic validation to prevent invalid input.

For example:

* Empty categories are rejected.
* Empty descriptions are rejected.
* Invalid numbers are rejected.
* Negative expense amounts are rejected.
* Invalid expense numbers cannot be deleted.

This makes the program more reliable and user-friendly.

---

## 🛠️ Technologies Used

* **Python 3**
* **JSON**
* **Command Line Interface (CLI)**

No external Python packages are required.

The project only uses Python's built-in `json` module.


## ⚠️ Current Limitations

This is a beginner-level command-line application, so it has some limitations.

Currently, the program:

* Does not have a graphical user interface.
* Does not support user accounts.
* Does not encrypt stored data.
* Does not record dates for expenses.
* Does not support editing an existing expense.
* Does not generate charts.
* Does not support multiple currencies.
* Does not provide monthly or yearly reports.

These limitations provide opportunities for future improvements.

---

## 🚀 Future Improvements

Possible improvements include:

### Expense Dates

Add a date to every expense so users can track spending over time.

### Edit Expenses

Allow users to modify an existing expense instead of deleting and recreating it.

### Monthly Reports

Create summaries showing spending for each month.

### Budget System

Allow users to set a monthly budget and receive warnings when spending approaches or exceeds the budget.

### Data Visualization

Add charts showing spending by category.

### Search and Filtering

Allow users to search for expenses by category, description, or date.

### Graphical User Interface

Build a GUI using a Python framework such as Tkinter.

### Database Storage

Replace JSON storage with a database such as SQLite as the project becomes more advanced.

---

## 📚 What I Learned

This project helped me understand how different Python concepts can work together to create a complete application.

One of the most important lessons was learning how to break a larger problem into smaller functions. Instead of putting the entire program into one large block of code, different responsibilities were separated into functions such as:

```text
add_expense()
view_expenses()
show_total()
show_categories()
delete_expense()
load_expenses()
save_expenses()
```

I also learned how programs can interact with files and preserve information after they are closed.

The project gave me practical experience with data structures, error handling, file management, and basic CRUD functionality.

---

## 🎓 Educational Purpose

This project is part of my Python programming practice and portfolio development.

Rather than focusing only on writing individual pieces of code, the project focuses on building a complete application from start to finish.

It represents a step toward developing larger projects involving software development, computer science, and eventually cybersecurity.

---

## 📄 License

This project is created for educational purposes. You are welcome to study, modify, and improve the code for your own learning.
