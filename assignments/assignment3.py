# Assignment 3 — Caesar Cipher Encrypt & Decrypt
# Due: Day 4 (Tomorrow)
#
# Instructions:
# 1. Ask for a message and shift number
# 2. Encrypt using Caesar Cipher (capital letters only)
# 3. Print the encrypted result
# 4. Decrypt the result and print it — should return to original
# 5. BONUS: Make it work with lowercase letters too

# Write your code below:
def encrypt(message, shift):
    # Your code here
    pass

def decrypt(cipher, shift):
    # Your code here
    pass

# Test it
msg = input("Message: ")
shift = int(input("Shift: "))
encrypted = encrypt(msg, shift)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, shift))
