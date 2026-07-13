# IWU Python Week: Encryption/Decryption App
## Instructor Guide - 5 Days

## Overview
Teach Python in 1 week. Final output: working encryption/decryption desktop app.

## Prerequisites
- Python 3.11+ installed on each student PC
- VS Code or any text editor
- `python -m pip install tkinter` (usually built-in)

---

## DAY 1 (Mon) - Foundations

### Hour 0.5: The Story of Python (15 min)

**Before typing anything - sit down, listen:**

**Why "Python"?**
- Creator: **Guido van Rossum** (Netherlands, 1989)
- He was reading the scripts of **Monty Python's Flying Circus** (a BBC comedy)
- He wanted a name that was "short, unique, and slightly mysterious"
- Not named after the snake! The snake logo came AFTER the name.

**The Zen of Python (Easter Egg)**
Tell students:
> "Before we write a single line, Python has a poem for you. Type this:"

```python
import this
```

Show output:
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
...
```

Ask students: *"What does this tell you about Python?"*
Answer: Python values **readability** and **simplicity** — it was designed to be easy to read.

**Why pip vs python -m pip**
- **pip** = Python's package installer (short for "Pip Installs Packages")
- But in newer Python (3.14+), typing just `pip` doesn't work because it's not in PATH
- **`python -m pip`** = "Python, run the pip module" — always works
- Rule of thumb: always use `python -m pip` (or `py -m pip` on Windows)

**IDE vs IDLE vs VS Code**
- **IDLE** = Built-in editor (comes with Python). Simple but limited
- **VS Code** = Professional editor. Has syntax highlighting, debugging, extensions
- **IDE** = Integrated Development Environment (VS Code, PyCharm, etc.)
- For this course: **VS Code** recommended

### Hour 1: Setup + Hello, Python

**Step 1: Check Python is installed**
Open Command Prompt (CMD), type:
```cmd
python --version
```

If you see `Python 3.11+`, you're good.

**Step 2: Open VS Code**
- Open VS Code
- Create a new file: `day1.py`
- Save it in a folder: `C:\IWU_Python\day1.py`

**Step 3: Your first Python program**
```python
# This is a comment - Python ignores this
# Your first program:

print("Hello, IWU!")
```

**Step 4: Run it**
- VS Code: click the "play" button (top right)
- Or in CMD: `python day1.py`

**The Zen of Python (run this together)**
```python
import this
```

**Variables:**
```python
name = "Juan"     # String (text)
age = 25           # Integer (whole number)
height = 5.9       # Float (decimal)
is_instructor = True  # Boolean (True/False)

print(name)
print(age)
print(height)
print(is_instructor)
```

**Data Types:**
```python
text = "Hello"     # <class 'str'>
number = 10        # <class 'int'>
decimal = 3.14     # <class 'float'>
is_ok = True       # <class 'bool'>

print(type(text))
print(type(number))
print(type(decimal))
print(type(is_ok))
```

**Exercise:** Print your name, rank, and branch of service.

### Hour 2: Strings
```python
# String operations
msg = "Information Warfare"
print(len(msg))        # 19
print(msg.upper())     # INFORMATION WARFARE
print(msg.lower())     # information warfare
print(msg[0])          # I
print(msg[-1])         # e
print(msg[0:3])        # Inf

# Input
name = input("Enter your name: ")
print("Hello,", name)
```

**Exercise:** Ask user for their name, print it backwards.

### Hour 3: ASCII & Numbers
```python
# ASCII - how computers store text
print(ord('A'))   # 65
print(ord('a'))   # 97
print(chr(65))    # A
print(chr(97))    # a

# Math operators
print(10 + 3)     # 13
print(10 - 3)     # 7
print(10 * 3)     # 30
print(10 / 3)     # 3.33
print(10 // 3)    # 3 (integer division)
print(10 % 3)     # 1 (remainder)
```

**Exercise:** Ask for a letter, print its ASCII value. Ask for a number, print its character.

### Hour 4: Practice Lab
Build a program that:
1. Asks user's name
2. Prints name in reverse
3. Prints ASCII value of first letter
4. Prints name in uppercase

---

## DAY 2 (Tue) - Logic & Loops

### Hour 1: If-Else
```python
# Conditions
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Multiple conditions
grade = int(input("Enter grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C")

# Checking characters
char = input("Enter a character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
else:
    print("Not a letter")
```

**Exercise:** Ask for a letter, tell if it's vowel or consonant.

### Hour 2: For Loops
```python
# Looping through strings
for letter in "HELLO":
    print(letter)

# Using range
for i in range(5):
    print(i)       # 0, 1, 2, 3, 4

for i in range(3, 7):
    print(i)       # 3, 4, 5, 6

# Loop with index
text = "IWU"
for i, letter in enumerate(text):
    print(i, letter)
```

**Exercise:** Print each letter of a word with its position.

### Hour 3: Building Strings with Loops
```python
# Building a new string
text = "hello"
result = ""
for letter in text:
    result += letter.upper()
print(result)      # HELLO

# Character shifting
text = "ABC"
shift = 1
result = ""
for letter in text:
    code = ord(letter) + shift
    result += chr(code)
print(result)      # BCD
```

**Exercise:** Shift each letter of "CAT" by 2 positions.

### Hour 4: Practice Lab
Build a program that:
1. Asks for a word
2. Counts how many vowels it has
3. Shifts each letter by 1
4. Prints original and shifted

---

## DAY 3 (Wed) - Caesar Cipher

### Hour 1: What is Encryption?
- Plaintext → Ciphertext → Decryption
- Why it matters for military/OPSEC
- Show example: "ATTACK" → "DWWDFN" (Caesar shift 3)

### Hour 2: Building the Shift (with wrap-around)
```python
# The problem: shifting past Z
print(chr(ord('Z') + 1))  # [ (not what we want)

# Solution: wrap-around using modulo
letter = 'Z'
shift = 1
if letter.isupper():
    base = ord('A')
result = chr((ord(letter) - base + shift) % 26 + base)
print(result)  # A
```

**Exercise:** Encrypt "XYZ" with shift 3 (should get "ABC").

### Hour 3: Complete Encrypt Function
```python
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # keep spaces, punctuation
    return result

# Test
print(encrypt("Hello, IWU!", 3))  # Khoor, LXZ!
```

### Hour 4: Decrypt + Challenge
```python
def decrypt(text, shift):
    return encrypt(text, -shift)

# Test
print(decrypt("Khoor, LXZ!", 3))  # Hello, IWU!

# Challenge: Brute force - decrypt without knowing shift
cipher = encrypt("Attack at dawn", 5)
for s in range(26):
    print(f"Shift {s}: {decrypt(cipher, s)}")
```

**Output:** Full working Caesar cipher with encrypt, decrypt, and brute force.

---

## DAY 4 (Thu) - XOR Cipher & Base64

### Hour 1: Binary & XOR Logic
```python
# Binary representation
print(bin(65))    # 0b1000001
print(ord('A'))   # 65

# XOR truth table
print(0 ^ 0)   # 0
print(1 ^ 1)   # 0
print(0 ^ 1)   # 1
print(1 ^ 0)   # 1

# XOR property: A XOR B XOR B = A
print(65 ^ 42 ^ 42)  # 65 (back to original!)
```

### Hour 2: XOR Cipher
```python
def xor_encrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

# XOR encrypt/decrypt are the same function!
msg = "Secret"
key = 42
encrypted = xor_encrypt(msg, key)
decrypted = xor_encrypt(encrypted, key)
print(encrypted, "->", decrypted)  # weird chars -> Secret
```

**Exercise:** Encrypt your name with key 75, decrypt to verify.

### Hour 3: Base64 Encoding
```python
import base64

# Encoding
text = "Hello, IWU!"
encoded = base64.b64encode(text.encode())
print(encoded)  # b'SGVsbG8sIElXVSE='

# Decoding
decoded = base64.b64decode(encoded).decode()
print(decoded)  # Hello, IWU!

# Why Base64? Binary data from XOR needs encoding for sharing
msg = "Secret Message"
key = 99
encrypted = xor_encrypt(msg, key)
safe = base64.b64encode(encrypted.encode()).decode()
print("Send this:", safe)
```

### Hour 4: Practice Lab - Menu System
Build a program with menu:
```
=== IWU CRYPT MENU ===
1. Caesar Encrypt
2. Caesar Decrypt
3. XOR Encrypt/Decrypt
4. Base64 Encode
5. Base64 Decode
6. Exit
Choice: _
```

---

## DAY 5 (Fri) - GUI App + Presentation

### Hour 1-2: Build the GUI
```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def encrypt_caesar():
    text = entry_text.get()
    shift = int(entry_key.get())
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    output.delete(1.0, tk.END)
    output.insert(1.0, result)

# Window setup
root = tk.Tk()
root.title("IWU Crypt v1.0")
root.geometry("500x400")
root.configure(bg="#1a1a2e")

# Widgets
tk.Label(root, text="Message:", fg="white", bg="#1a1a2e").pack(pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)

tk.Label(root, text="Key:", fg="white", bg="#1a1a2e").pack(pady=5)
entry_key = tk.Entry(root, width=20)
entry_key.pack(pady=5)

tk.Button(root, text="Encrypt (Caesar)", command=encrypt_caesar,
          bg="#c00", fg="white").pack(pady=10)

tk.Label(root, text="Output:", fg="white", bg="#1a1a2e").pack(pady=5)
output = tk.Text(root, height=8, width=50)
output.pack(pady=5)

root.mainloop()
```

### Hour 3: Complete All Cipher Functions
Add XOR encrypt/decrypt, Base64 encode/decode, file save/load.

### Hour 4: Testing + Presentation
- Each student encrypts a message
- Swaps with classmate
- Decrypts classmate's message
- Present working app

### Hour 5: Course Wrap-Up
- What they learned
- Why encryption matters for IWU
- OPSEC takeaway: encrypted comms, password security
- Certificate/token of completion

---

## Final App Features
- Caesar Encrypt/Decrypt (with key)
- XOR Encrypt/Decrypt (key-based, same function)
- Base64 Encode/Decode
- Copy output to clipboard
- Save to .txt file
- Load from .txt file
- Dark theme military-style UI
