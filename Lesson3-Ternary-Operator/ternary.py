# JS Ternary
"""
Let status = age >= 18 ? 'adult': 'minor'
let message = score >- 90? "Excellent" : "Keep trying
"""
# Python Ternary
age = 15
status = "adult" if age >= 18 else "minor"
score = 75
message = "Excellent" if score >= 90 else "Keep Trying!"


# Examples
password = "mypass123"
strength = "Strong" if len(password) >= 8 else "Weak"
print(f"Password: {password}/n Strength: {strength}")

# Combining Ternary + Chaining
category = (
    "Child"
    if 0 <= age <= 12
    else "teen" if 13 <= age <= 19 else "Adult" if age >= 20 else "Senior"
)


score = 67
grade = (
    "A" if score >= 90
    else "B" if score >= 80 else "c" if score >= 70 else "D" if score >= 60 else "F"
)

