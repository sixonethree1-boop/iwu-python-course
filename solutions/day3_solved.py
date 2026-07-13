# Day 3 - Solved: Caesar Cipher

def encrypt(text, shift):
    """Encrypt text using Caesar cipher with given shift"""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces and punctuation
    return result

def decrypt(text, shift):
    """Decrypt text by shifting backwards"""
    return encrypt(text, -shift)

# Test
print("=== Caesar Cipher Test ===")
plain = "Attack at dawn!"
key = 5
cipher = encrypt(plain, key)
print(f"Plain:  {plain}")
print(f"Shift:  {key}")
print(f"Cipher: {cipher}")
print(f"Decrypted: {decrypt(cipher, key)}")

# Brute force cracker
print("\n=== Brute Force (try all 25 shifts) ===")
secret = encrypt("Secret message here", 13)
print(f"Secret message: {secret}\n")
for s in range(26):
    guess = decrypt(secret, s)
    if s == 13:
        print(f">>> Shift {s}: {guess} (CORRECT)")
    else:
        print(f"  Shift {s}: {guess}")
