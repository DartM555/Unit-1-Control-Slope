# text = "Hello World"
# count=0
# for char in text:
#     if char == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
#         count += 1
#         print(f"{char} is a vowel")
        
# Answer:
# text = "Hello World"
# vowels = "aeiouAEIOU"
# for char in text:
#     if char in vowels:
#         vowel_count += 1
#         print(f"Vowels in '{text}': {vowel_count}")
        
# text = "ABC123xyz" 
# for i in range(len(text)):
#     if '0' <= text[i] <= '9':
#         print(f" Digit is at position {i}: {text[i]}")
        
word = "Hello"
for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {-1-i}")
  
