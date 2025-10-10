# Pyramid Pattern
# Row 0: 4 spaces, 1 star => 0 spaces, 9 stars

rows = 5
spaces = rows - 1
for row in range(1, rows + 1):
   for space in range(spaces):
       print(" ", end="")
       
       spaces -= 1
       for stars in range(1, 2 * row):
           print("*", end="")
           print()
        




9
