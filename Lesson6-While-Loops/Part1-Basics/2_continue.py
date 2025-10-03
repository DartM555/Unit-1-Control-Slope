# Continue statement
'''
**continue** = skip to the next iteration
**difference from break:**
**break => exit the loop comepletely**
**contimue => skip to the next iteration**
'''

count = 0
while count < 5:
    count += 1
    if count == 3:
         continue
    print(count) # 1 2 4 5
         