# Pyramid Pattern


rows = 5

spaces = rows - 1
for row in range(1, rows + 1):
   for space in range(spaces):
       print(" ", end="")
       
       spaces -= 1
       for stars in range(1, 2 * row):
           print("*", end="")
           print()
        
        
# Mr Gemici's Example

rows = 5
# create an outer loop for the rows

for i in range(rows):
    #Step 2: print the spaces -- rows - i - 1
    for j in range(rows-i-1):
        print(" ", end ="")
        # Step 3: print the stars -- 2*1+1
        for k in range(2*i+1):
         print("*", end="")
        #  Step 4: print a new line
        print()