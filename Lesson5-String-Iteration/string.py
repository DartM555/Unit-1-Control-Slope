# String indexing and slicing
# ====================================
word = "Python"
#       012345 (positive indexing)
word[0] # P (first character)
word[1] # y (second character)
word[5] # n (last character)
word[-1] # n (last character)
len(word) #Length of the string
word(len(word)-1) # in las character

# String Slicing
# =====================================
word[0:3] #Pyt (character 0,1,2)
word[:3] #Pyt (character 0,1,2)
word[2:5] #tho (character 2,3,4)
word[2:6] #thon (character 2,3,4,5)
len(word) #thon (characters 2,3,4,5)
word[2:] #thon (characters 2,3,4,5)

word[-3] #hon (character -3,-2,-1 pr 3,4,5)

#Part One-String iteration Patterns
# =====================================
#Direct character iteration
for char in word:
    print(char)
    
    # Index based iteration
    for i in range(len(word)):
        print(word[i])
        
        # Character Classification
        # =====================================
# char = input("Press a key")
# # Check characters type using ASCII ranges
# if 'A' <= char <= 'Z':
#     print(f"{char} is an uppercase")
# if 'A' <= char <= 'z': 
#     print(f"{char} is an lowercase")
# if '0' <= char <= '9': 
#     print(f"{char} is an digit")
# letter detection 
char = input("Press a key")
if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
    print(f"{char} is a letter")
else:
    print("Please choose a letter")
    