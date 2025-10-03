# Break statement in loops
# break - exit the loop immediately
# Use cases: 
''' 
*Stop when you find something
*Exit early based on condition
*Get out of infinite loop
'''

# count = 1
# while count <= 10:
#     print(count)
#     if count == 5:
#         break
#     count += 1


# while True: 
#     choice = input("Enter something: (q for quit)")
#     if choice == 'q':
#         print("You want to exit!")
#         break
#     print(f"You entered: {choice}")
    
    # Algorithm: find first divisor
n = 15
divisor = 2
while divisor < n:
    if n % divisor == 0:
        break
    divisor += 1
    print(divisor)