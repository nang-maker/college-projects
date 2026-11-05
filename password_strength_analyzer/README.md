# 🔐 Password Strength Analyzer

A beginner-friendly Python command-line application that analyzes the strength of a password based on its length and character composition.

The program checks whether a password contains uppercase letters, lowercase letters, numbers, and symbols. It then uses these characteristics to calculate a simple strength score and classifies the password as **Weak**, **Medium**, or **Strong**.

This project was created as an introduction to Python programming and basic cybersecurity concepts, particularly the importance of creating stronger passwords.

---

## 📌 Project Overview

Passwords are one of the most common ways users protect their accounts. However, passwords that are short or use only one type of character can be easier to guess.

The Password Strength Analyzer provides a simple way to evaluate a password's basic characteristics.

The application asks the user to enter a password and analyzes:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

Based on these characteristics, the program calculates a score and provides a basic strength classification.

---

## 🎯 Project Goals

The main goal of this project was to practice fundamental Python programming while exploring a simple cybersecurity-related problem.

Through this project, I practiced:

* Variables
* Boolean values
* Strings
* Loops
* Conditional statements
* User input
* String methods
* Basic program logic
* Functions and program organization
* Designing a simple scoring system

---

## ✨ Features

### Password Analysis

The program checks whether the password contains:

| Character Type | Example       |
| -------------- | ------------- |
| Uppercase      | `A`, `B`, `C` |
| Lowercase      | `a`, `b`, `c` |
| Number         | `1`, `2`, `3` |
| Symbol         | `!`, `@`, `#` |

It also calculates the total password length.

---

### Strength Score

The program awards one point for each condition that is satisfied:

* Length of at least 8 characters → **+1**
* Contains uppercase letters → **+1**
* Contains lowercase letters → **+1**
* Contains numbers → **+1**
* Contains symbols → **+1**

The resulting score is classified as:

```text
0–2  → Weak
3–4  → Medium
5    → Strong
```

---

## 🖥️ Example

Example input:

```text
Enter your password: Hello123!
```

Example output:

```text
Password Analysis
-------------------------
Length: 9
Uppercase: True
Lowercase: True
Numbers: True
Symbols: True
Strength: Strong
```

---

## 🛠️ Technologies Used

* **Python 3**
* Python string methods
* Command Line Interface (CLI)

No external libraries are required.

---

## 📂 Project Structure

```text
password-strength-analyzer/
│
├── main.py
├── README.md
└── .gitignore
```

### `main.py`

Contains the complete password analysis program.

### `README.md`

Contains documentation about the project.

### `.gitignore`

Contains files that should not be uploaded to the repository.

---

## ▶️ How to Run

Make sure Python 3 is installed.

Check the installation with:

```bash
python --version
```

or on Windows:

```bash
py --version
```

Run the program using:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

Then enter a password when prompted.

---

## 🔐 Security Note

This project is an **educational password-strength demonstration**, not a professional password security tool.

The program does not measure the true security of a password or calculate how long it would take to crack.

It only evaluates several basic characteristics of the password.

For example, a password could contain uppercase letters, lowercase letters, numbers, and symbols and still be predictable.

The program also does not store or transmit passwords.

For real applications, password security should involve additional techniques such as secure password hashing, password managers, rate limiting, and protection against common or compromised passwords.

---

## ⚠️ Limitations

The current version has several limitations:

* It uses a simple scoring system.
* It does not check password length beyond the 8-character requirement.
* It does not detect common passwords.
* It does not check whether a password has appeared in known data breaches.
* It does not estimate password entropy.
* It does not detect predictable patterns.
* It does not provide secure password storage.

These limitations provide opportunities for future development.

---

## 🚀 Future Improvements

Possible improvements include:

* Adding a password generator
* Checking passwords against a list of common passwords
* Detecting repeated characters
* Detecting predictable sequences
* Calculating password entropy
* Providing suggestions for improvement
* Creating a graphical user interface
* Adding more detailed security recommendations

---

## 📚 What I Learned

This project was one of my first Python projects with a cybersecurity focus.

I learned how to examine individual characters in a string using a loop and Python's built-in string methods such as:

```python
char.isupper()
char.islower()
char.isdigit()
char.isalnum()
```

I also learned how Boolean variables can be used to keep track of whether certain conditions are present.

Most importantly, this project helped me understand how simple programming logic can be applied to a cybersecurity-related problem.

---

## 🎓 Educational Purpose

This project was created as part of my programming practice and undergraduate portfolio preparation.

It represents an early step in exploring the relationship between programming and cybersecurity.

The project focuses on understanding fundamental programming concepts rather than creating a production-level security system.

---

## 📄 License

This project is created for educational purposes. You are welcome to study, modify, and improve the code for learning.
