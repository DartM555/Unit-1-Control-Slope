# Pyramid Pattern
# Row 0: 4 spaces, 1 star => 0 spaces, 9 stars

rows = 5
for i in range(rows):
    for j in range(rows-i-1):
        print(" " , end = "")
        for k in range(2*i+1):
            print("*")
    
