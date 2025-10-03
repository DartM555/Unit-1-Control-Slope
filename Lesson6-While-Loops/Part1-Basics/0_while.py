# # Count down from 5
# # num = 5
# # while num > 0:
# #     num -= 1
# #     print(num)
# # print("Blastoff!")


# # # # Add sums of numbers 1 to 10
# # num = 1
# # total = 0

# # # while num <= 10:
# # #     total += num
# # #     num += 1
# # #     print(f"Total: {total}")

# # while num <= 10:
# #     total += num
# #     if num < 10:
# #         print(num, end = "+")
# #     else:
# #         print(num, end = "=")
# #         num += 1
# #         print(total)

# # Sum of digits
# # Take a user input as int, and sum the digit of it
# number = input("Enter a number:") #1234
# sum = 0
# # for char in number: 
# #     print(f"{char} {type(char)}")
# #     sum += int(char)
# #     print(f"Total: {sum}")
    
# i= 0
# while i < len(number):
#     sum += int(number[i])
#     i += 1
#     print(f"Total: {sum}")

# Algorithm - sum of digits(as int)
# n = int(input("Enter a number:"))
# number = n
# sum = 0
# while number > 0:
#     digit = number % 10 #Get the last digit
#     sum += digit #add to sum
#     number = number // 10 #Remove the last digit
    
#     print(f"The sum of digits {n} is {sum}")
    

# Algorithm - count digits (as int)
number = 54321
count = 0

while number > 0:
    count += 1
    number = number // 10
    print(f"The number {number} has {count} of digits")
    
    n = 7
   