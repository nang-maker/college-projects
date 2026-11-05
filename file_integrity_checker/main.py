import hashlib
import json


# Calculate the SHA-256 hash of a file
def calculate_hash(file_path):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        return hashlib.sha256(file_data).hexdigest()

    except FileNotFoundError:
        print("\nError: The file could not be found.")
        return None


# Create and save a baseline hash
def create_baseline():
    file_path = input("\nEnter the path of the file: ")

    file_hash = calculate_hash(file_path)

    if file_hash is None:
        return

    try:
        with open("integrity.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {}

    except json.JSONDecodeError:
        print("\nError: integrity.json contains invalid data.")
        return

    data[file_path] = file_hash

    with open("integrity.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nBaseline created successfully! ✅")
    print("File:", file_path)
    print("SHA-256:", file_hash)


# Check whether the file has been modified
def check_integrity():
    try:
        with open("integrity.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("\nError: No baseline exists yet.")
        print("Create a baseline first.")
        return

    except json.JSONDecodeError:
        print("\nError: integrity.json contains invalid data.")
        return

    file_path = input("\nEnter the path of the file: ")

    if file_path not in data:
        print("\nError: No baseline exists for this file.")
        print("Create a baseline for this file first.")
        return

    original_hash = data[file_path]

    current_hash = calculate_hash(file_path)

    if current_hash is None:
        return

    print("\n===== File Integrity Check =====")

    if current_hash == original_hash:
        print("Status: File is unchanged ✅")
    else:
        print("Status: WARNING - File has been modified! ⚠️")

    print("\nOriginal Hash:")
    print(original_hash)

    print("\nCurrent Hash:")
    print(current_hash)

# Main menu
while True:
    print("\n================================")
    print("      FILE INTEGRITY CHECKER")
    print("================================")
    print("1. Create baseline")
    print("2. Check file integrity")
    print("3. Exit")
    print("================================")

    choice = input("Choose an option: ")

    if choice == "1":
        create_baseline()

    elif choice == "2":
        check_integrity()

    elif choice == "3":
        print("\nGoodbye! Stay secure. 🔐")
        break

    else:
        print("\nInvalid choice. Please choose 1, 2, or 3.")