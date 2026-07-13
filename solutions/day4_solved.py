# Day 4 - Solved: XOR Cipher + Base64

import base64

def xor_encrypt(text, key):
    """XOR encrypt/decrypt (same function for both operations)"""
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

def xor_encrypt_safe(text, key):
    """XOR encrypt with Base64 encoding for safe sharing"""
    raw = xor_encrypt(text, key)
    return base64.b64encode(raw.encode()).decode()

def xor_decrypt_safe(encoded_text, key):
    """Decrypt Base64-encoded XOR ciphertext"""
    raw = base64.b64decode(encoded_text).decode()
    return xor_encrypt(raw, key)

# Test
print("=== XOR Cipher Test ===")
msg = "Secret Message"
key = 99
encrypted = xor_encrypt(msg, key)
decrypted = xor_encrypt(encrypted, key)
print(f"Original: {msg}")
print(f"Key: {key} ({chr(key)})")
print(f"Encrypted (raw): {repr(encrypted)}")
print(f"Decrypted: {decrypted}")
print(f"Match: {msg == decrypted}")

print("\n=== XOR + Base64 (Safe for Sharing) ===")
safe = xor_encrypt_safe(msg, key)
print(f"Encrypted (base64): {safe}")
back = xor_decrypt_safe(safe, key)
print(f"Decrypted: {back}")

print("\n=== Menu System ===")
def menu():
    while True:
        print("\n=== IWU CRYPT MENU ===")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt")
        print("3. XOR Encrypt/Decrypt")
        print("4. Base64 Encode")
        print("5. Base64 Decode")
        print("6. Exit")
        
        choice = input("Choice: ").strip()
        if choice == "6": break
        
        text = input("Text: ").strip()
        
        if choice in ("1", "2"):
            shift = int(input("Shift (0-25): ") or "3")
            from solutions.day3_solved import encrypt, decrypt
            if choice == "1": print(f"Result: {encrypt(text, shift)}")
            else: print(f"Result: {decrypt(text, shift)}")
        elif choice == "3":
            key = ord(input("Key character: ") or "K")
            result = xor_encrypt(text, key)
            safe = base64.b64encode(result.encode()).decode()
            print(f"Raw: {repr(result)}")
            print(f"Base64 safe: {safe}")
            print(f"Decrypt verify: {xor_encrypt(result, key)}")
        elif choice == "4":
            print(f"Encoded: {base64.b64encode(text.encode()).decode()}")
        elif choice == "5":
            try:
                print(f"Decoded: {base64.b64decode(text).decode()}")
            except:
                print("Invalid Base64!")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
