# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("Student Information:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()

# TODO: Check if age is valid (between 16 and 100)
if 16 <= age <= 100:
    print("Your age is valid.")
else:
    print("Your age is not valid.")

# TODO: Check if GPA is valid (between 0.0 and 4.0)
if 0.0 >= gpa <= 4.0:
    print("Your GPA is valid")

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
if age >= 18 and gpa >= 2.0:
    print("You are eligible for enrollment.")
else:
    print("You are not eligible for enrollment.")

# TODO: Check voting eligibility (age >= 18)
if age >= 18:
    print("You are eligible to vote.")

# TODO: Check honor roll status (gpa >= 3.5)
if gpa >= 3.5:
    print("You are on the honor roll!")