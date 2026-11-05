# 🛡️ File Integrity Checker

A Python command-line application that uses **SHA-256 hashing** to detect whether a file has been modified.

The program creates a digital fingerprint of a file and saves the fingerprint as a baseline. When the file is checked again, the program calculates a new fingerprint and compares it with the original.

If the fingerprints are identical, the file is considered unchanged. If they are different, the program warns that the file may have been modified.

This project introduces a fundamental cybersecurity concept: **file integrity monitoring**.

---

## 📌 Project Overview

Files can sometimes be modified without the owner immediately noticing. In cybersecurity, checking whether important files have changed can help identify unexpected or unauthorized modifications.

A cryptographic hash provides a convenient way to represent the contents of a file.

The File Integrity Checker uses the SHA-256 hashing algorithm to create this representation.

The basic process is:

```text
File
 ↓
SHA-256 Hash
 ↓
Save original hash
 ↓
Check file later
 ↓
Calculate new hash
 ↓
Compare hashes
 ↓
Same → Unchanged
Different → Modified
```

---

## 🎯 Project Goals

The main goal of this project was to learn how a basic cybersecurity tool can be built using Python.

Through this project, I practiced:

* File handling
* Reading binary files
* SHA-256 hashing
* JSON data storage
* Functions
* Conditional statements
* Exception handling
* Comparing data
* Command-line application design

---

## 🔐 How Hashing Works

A cryptographic hash function takes data and produces a fixed-length value called a **hash**.

For example:

```text
File contents
     ↓
  SHA-256
     ↓
Digital fingerprint
```

If the contents of the file change, the resulting hash will normally change as well.

For example:

```text
Original file
     ↓
SHA-256
     ↓
ABC123...
```

After modification:

```text
Modified file
     ↓
SHA-256
     ↓
XYZ789...
```

Because the hashes are different, the program can identify that the file has changed.

---

## ✨ Features

### 1. Create a Baseline

The user can select a file and generate its SHA-256 hash.

The hash is then saved as the trusted baseline.

---

### 2. Check File Integrity

The program calculates the file's current SHA-256 hash and compares it with the saved baseline.

If they match:

```text
Status: File is unchanged ✅
```

If they do not match:

```text
Status: WARNING - File has been modified! ⚠️
```

---

### 3. JSON Storage

The baseline information is stored in a JSON file.

Example:

```json
{
    "test.txt": "a591a6d40bf420404a011733cfb7b190..."
}
```

This allows the program to remember the original hash after it has been closed.

---

### 4. Error Handling

The program handles common problems such as:

* Missing files
* Missing baseline information
* Invalid JSON data

Instead of immediately displaying a Python traceback, the program provides a simple error message to the user.

---

## 🖥️ Example

The application provides a simple command-line interface:

```text
================================
      FILE INTEGRITY CHECKER
================================
1. Create baseline
2. Check file integrity
3. Exit
================================
Choose an option:
```

After creating a baseline, checking an unchanged file may produce:

```text
===== File Integrity Check =====
Status: File is unchanged ✅
```

If the file has been modified:

```text
===== File Integrity Check =====
Status: WARNING - File has been modified! ⚠️
```

---

## 🛠️ Technologies Used

* **Python 3**
* `hashlib`
* `json`
* Command Line Interface (CLI)

Both `hashlib` and `json` are included in Python's standard library, so no external packages are required.

---

## 📂 Project Structure

```text
file-integrity-checker/
│
├── main.py
├── integrity.json
├── test.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains the main File Integrity Checker application.

### `integrity.json`

Stores baseline hash information.

### `test.txt`

A sample file used for testing the application.

### `README.md`

Contains documentation about the project.

### `.gitignore`

Prevents files that should remain local from being uploaded to GitHub.

---

## ▶️ How to Run

Make sure Python 3 is installed.

Check your installation:

```bash
python --version
```

or:

```bash
py --version
```

Run the application:

```bash
python main.py
```

---

## 🧪 Testing

The application can be tested by creating a small text file.

For example:

```text
test.txt
```

Add some text:

```text
Hello, cybersecurity!
```

Create a baseline for the file.

Then check its integrity without changing the file.

The program should report:

```text
File is unchanged ✅
```

Next, change the contents of the file:

```text
Hello, cybersecurity!!
```

Save it and check the file again.

The program should detect the difference:

```text
WARNING - File has been modified! ⚠️
```

This demonstrates how changing even a small part of a file can produce a different hash.

---

## 🔒 Security Note

This project demonstrates the basic concept of file integrity checking. It is not intended to replace professional file-integrity monitoring or security software.

SHA-256 can help detect changes to file contents, but the security of the overall system also depends on protecting the stored baseline.

For example, if an attacker can modify both the file and its stored baseline hash, a simple checker may not detect the change.

Professional systems can use additional protections such as secure storage, access controls, monitoring, and centralized logging.

---

## ⚠️ Limitations

The current version is intentionally simple.

It does not currently provide:

* Real-time file monitoring
* Automatic alerts
* Digital signatures
* Encryption
* A graphical interface
* Centralized logging
* Advanced access control
* Protection against an attacker who can modify the baseline

These features could be explored in more advanced versions.

---

## 🚀 Future Improvements

Possible improvements include:

* Monitoring multiple files
* Displaying all monitored files
* Adding file and directory selection
* Adding timestamps
* Providing detailed change reports
* Creating a graphical interface
* Adding real-time monitoring
* Generating security logs
* Using digital signatures to protect baseline information

---

## 📚 What I Learned

This project introduced me to one of the fundamental concepts used in cybersecurity: **cryptographic hashing**.

I learned how Python's `hashlib` module can be used to generate a SHA-256 hash and how the hash can act as a fingerprint for file contents.

I also learned how to read files, store information using JSON, compare values, and handle errors.

The project helped me understand an important security principle:

> **Instead of examining every part of a file manually, we can compare its cryptographic fingerprint to detect changes.**

---

## 🎓 Educational Purpose

This project was created as part of my Python programming and cybersecurity learning journey.

It builds upon basic programming concepts and introduces a practical cybersecurity application.

The project is intentionally designed at a beginner-to-intermediate level so that the underlying concepts can be understood and explained clearly.

---

## 📄 License

This project is created for educational purposes. You are welcome to study, modify, and improve the code for learning.
