height = int(input("Enter your height in inches:"))
weight = int(input("Enter your weight in pounds:"))

bmi = (weight / (height * height)) * 703

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
    
        

