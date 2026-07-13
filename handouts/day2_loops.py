# Day 2 - Student Handout
# Name: _________________   Date: _________

# === 1. If-Else ===
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# --- Your turn ---
# Ask for a letter, tell if it's uppercase or lowercase
letter = input("Enter a letter: ")
# TODO: Use if-else to check letter.isupper()
if     :
    print("Uppercase")
else:
    print("Lowercase")


# === 2. Vowel or Consonant? ===
char = input("Enter a letter: ").lower()
# TODO: Check if char is in "aeiou"
if     :
    print("Vowel")
else:
    print("Consonant")


# === 3. For Loops ===
for letter in "HELLO":
    print(letter)

# --- Your turn ---
word = input("Enter a word: ")
# TODO: Print each letter on a separate line
for     :


# === 4. Loop with Index ===
text = "IWU"
for i, letter in enumerate(text):
    print(i, letter)

# --- Your turn ---
word = input("Enter a word: ")
# TODO: Print each letter with its position (0, 1, 2...)
for     :


# === 5. Building Strings ===
text = "hello"
result = ""
for letter in text:
    result += letter.upper()
print(result)  # HELLO

# --- Your turn ---
word = input("Enter a word: ")
# TODO: Build a string where each letter is shifted by 1
# Hint: chr(ord(letter) + 1)
result = ""
for letter in word:
    
print("Shifted:", result)


# === 6. FINAL CHALLENGE ===
# Write a program that:
# 1. Asks for a word
# 2. Counts how many vowels it has
# 3. Shifts each letter by 2
# 4. Prints original and shifted

word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0
# TODO: Count vowels
for letter in word:
    if     :
        count += 1

# TODO: Shift each letter by 2
shifted = ""
for letter in word:
    if letter.isalpha():
        shifted += 
    else:
        shifted += letter

print(f"Original: {word}")
print(f"Vowels: {count}")
print(f"Shifted (+2): {shifted}")
