# Activity 1: Steps to Brush Teeth

# Activity 2:Interactive Greeting
color = input("What is your favorite color? ")
print(f"Wow, I also like {color}!")

# Activity 3: Number Checker (check whether a number is positive, negative, or zero)
number = int(input("Enter a number: "))
if number < 0:
    print("Negative")
elif number > 0:
    print("Positive")

# Activity 4: Odd or Even Game
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd") 
    
    # 6: -----------

# Activity 7: Movie Ticket Price

age = int(input("Enter your age: "))
if age > 13:
    print("Child Ticket: $8")
elif 14 > age < 60:
    print("Adult Ticket: $12")
else:
    print("Senior Ticket: $10")
