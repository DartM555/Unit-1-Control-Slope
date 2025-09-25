# Dispenser Example
money = int(input("How much money do you have? "))

if money < 2:
    print("Not enough money.")
elif money == 2:
    print("Dispense Snack.")
elif money > 2:
    print("Dispense Snack + Change.")
