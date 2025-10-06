# Input Validation  1 - Username validation
while True:
    username = input("Enter a username (3-15 characters):")  
    if len(username) < 3:
        print("Too short! Min 3 characters!")
        continue
    if len(username) > 15:
        print("Too long! Max 15 characters!")
        continue
    # Check if username has any spaces
    has_space = False
    for char in username:
        if char == ' ':
            has_space = True
            break
    if has_space:
        print("No spacese allowed!") 
        continue
    # username validatoin passed
    print(f"Username '{username}' accepted!\n")
        
