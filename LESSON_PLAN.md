# IWU Python Week: Encryption/Decryption App
## Instructor Guide - 5 Days

## Overview
Teach Python in 1 week. Final output: working encryption/decryption desktop app.

## Prerequisites
- Python 3.11+ installed on each student PC
- VS Code or any text editor
- `python -m pip install tkinter` (usually built-in)

---

## DAY 1 (Mon) — Foundations

### Hour 0: Setup — Installing Python

**Windows (via Command Prompt / PowerShell):**

Hindi recommended ang `winget` kasi hindi lahat ng Windows version ay may `winget`. Gamitin ang manual download:
1. Puntahan: `python.org/downloads`
2. I-download ang latest **Python 3.11+** (Windows installer)
3. **CHECK** ang box: *"Add Python to PATH"* — ito ang pinakamahalaga
4. Click **Install Now**
5. I-verify:
```cmd
python --version
```

**Windows (via Terminal — using winget kung available):**
```powershell
winget install Python.Python.3.11
python --version
```
> ⚠️ **Kung walang winget:** Gamitin ang manual download sa ibaba.

**Windows (manual — sureball, gumagana sa lahat):**
1. Buksan ang browser: `python.org/downloads`
2. I-click ang **Download Python 3.11.x** (yellow button)
3. Patakbuhin ang installer
4. **✅ CHECK** ang *"Add Python to PATH"* (ibaba ng window)
5. Click **Install Now**
6. I-verify sa CMD:
```cmd
python --version
```

**Mac (via Terminal):**

**Option A — Homebrew (recommended):**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.11
python3 --version
```

**Option B — Xcode Command Line Tools (built-in, pero luma ang version):**
```bash
xcode-select --install
python3 --version
```

**Option C — Manual installer:**
1. Puntahan: `python.org/downloads`
2. I-download ang **macOS installer** (64-bit universal2)
3. I-install
4. I-verify:
```bash
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip -y
python3 --version
```

### Hour 0.5: IDLE vs IDE — Saan ka magsusulat ng code?

| Tool | Uri | Para sa |
|---|---|---|
| **IDLE** | **Integrated DeveLopment Environment** (built-in) | Simpleng testing, beginner-friendly, kasama na ng Python |
| **VS Code** | **IDE** (by Microsoft) | Professional coding, may extensions, color coding |
| **PyCharm** | **IDE** (by JetBrains) | Heavy-duty Python development |
| **Notepad++** | Text editor lang | Walang special features, pang-edit lang |

**Para sa klase natin — VS Code ang gagamitin natin.**

**I-install ang VS Code:**
1. Puntahan: `code.visualstudio.com`
2. I-download at i-install
3. Buksan ang VS Code
4. I-install ang **Python extension** (Python by Microsoft) — left sidebar, click Extensions icon, search "Python"
5. Gumawa ng bagong file → Save as `test.py`
6. I-type: `print("Hello, IWU!")`
7. I-run: Right-click → **Run Python File in Terminal**

### Hour 1: The Zen of Python

Bago tayo mag-code, basahin muna natin ang **pilosopiya ng Python**. Ito ang gumagabay sa lahat ng Python developers.

Open **Python interpreter** sa terminal:
```
python
```

I-type:
```python
import this
```

Lalabas ito:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
### Hour 1.5: Your First Python Program

Sa VS Code, gumawa ng bagong file: `first.py`

I-type:
```python
# My first Python program
print("Hello, IWU!")
```

**I-run:** Right-click → **Run Python File in Terminal**

Output: `Hello, IWU!`

**Congratulations.** Unang Python program mo na yan.

### Hour 2: Variables and Data Types

Sa VS Code, gumawa ng bagong file: `day1.py`

**Variables — parang lalagyan ng datos**

```python
# String (text)
name = "Juan"
print(name)

# Integer (whole number)  
age = 25
print(age)

# Float (decimal)
height = 5.9
print(height)

# Boolean (True/False)
is_marine = True
print(is_marine)
```

**Data Types activity:** I-type ito isa-isa:

```python
print(type("Hello"))     # <class 'str'>
print(type(25))          # <class 'int'>  
print(type(5.9))         # <class 'float'>
print(type(True))        # <class 'bool'>
```

**String Operations — importante para sa OSINT data cleaning:**

```python
msg = "Information Warfare Unit"
print(msg.upper())        # INFORMATION WARFARE UNIT
print(msg.lower())        # information warfare unit
print(msg.count("a"))     # 2
print(msg.split())        # ['Information', 'Warfare', 'Unit']
```

### Hour 3: User Input at Type Conversion

```python
name = input("Ano pangalan mo? ")
print("Hello, " + name + "!")

# input() returns STRING — kailangan iconvert
age = input("Ilang taon ka na? ")
age_num = int(age)
next_year = age_num + 1
print("Next year: " + str(next_year))
```

### Hour 4: Hands-on — IWU Profile Card

```python
# IWU Profile Card
print("=== IWU PROFILE ===")
name = input("Pangalan: ")
rank = input("Rank: ")
years = int(input("Years in service: "))
expertise = input("Expertise (OSINT/Cyber/Analysis): ")

print("\n===== IWU MEMBER =====")
print("Name: " + name)
print("Rank: " + rank)
print("Years: " + str(years))
print("Expertise: " + expertise)
print("Status: " + ("Veteran" if years >= 5 else "Junior"))
print("======================")
```

**Day 1 Takeaway:** Print, variables, input, type conversion — foundation ng lahat ng Python tools na gagawin natin this week.

---

**📚 READING ASSIGNMENT — Due Day 2 (Tomorrow)**

**Read:** `handouts/day1_basics.py` — buksan sa VS Code, basahin ang comments, i-run ang code.

**Challenge:** Gumawa ng bagong file `assignment1.py` na:
1. Mag-ask ng **full name** ng user
2. Mag-ask ng **favorite OSINT tool** (ex: Facebook, Twitter, Telegram)
3. I-print ang: `"[Name] specializes in [tool] intelligence."`
4. I-print kung ilang characters ang name
5. I-print ang name sa UPPERCASE

**Submit:** Save ang `assignment1.py` at ipasa kinabukasan bago mag-umpisa ang klase.

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
**Exercises:**
1. Ask user for age, tell if they are senior (60+), adult (18-59), or minor (below 18)
2. Ask for a number, print all numbers from 1 to that number
3. Ask for a word, print each letter on a new line

---

**📚 READING ASSIGNMENT — Due Day 3 (Tomorrow)**

**Read:** `handouts/day2_loops.py` — buksan at i-run. Pansinin ang pagkakaiba ng `for` at `while`.

**Challenge:** Gumawa ng `assignment2.py`:
1. Mag-ask ng **secret message**
2. Mag-ask ng **shift number** (1-26)
3. I-loop ang bawat letter at i-shift gamit ang `ord()` at `chr()`
4. I-print ang **naka-encrypt na mensahe**
5. I-print ang **original message**

**Submit:** `assignment2.py` kinabukasan.

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

### Hour 4: ASCII & Unicode Discussion
**Why ASCII matters for encryption:** Encryption works by manipulating numbers. ASCII lets us convert letters to numbers and back.
- `ord('A')` = 65
- `chr(65)` = 'A'

---

**📚 READING ASSIGNMENT — Due Day 4 (Tomorrow)**

**Read:** Review ang Caesar Cipher code sa Day 3 lesson.

**Challenge:** `assignment3.py` — Gawing **mas secure** ang Caesar Cipher:
1. Mag-ask ng message at shift number
2. I-encrypt gamit ang Caesar Cipher (capital letters lang)
3. I-print ang encrypted result
4. I-decrypt ang result at i-print — dapat bumalik sa original
5. **Bonus:** Gawing gumagana rin sa lowercase letters

**Submit:** `assignment3.py` kinabukasan.

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

**📚 READING ASSIGNMENT — Due Day 5 (Tomorrow - Final Day)**

**Read:** Review lahat ng codes mula Day 1 hanggang Day 4.

**Challenge:** `assignment4.py` — Pagsamahin ang lahat:
1. GUI na may **textarea** para sa message
2. **Entry** para sa key
3. Buttons: **Encrypt (Caesar)**, **Encrypt (XOR)**, **Decrypt**
4. Output area
5. Dark theme (bg black, text white)

**Submit:** `assignment4.py` kinabukasan — final app na ito.

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
