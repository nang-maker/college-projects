password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_symbol = True

length = len(password)

score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Analysis")
print("-" * 25)
print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Numbers:", has_digit)
print("Symbols:", has_symbol)
print("Strength:", strength)
