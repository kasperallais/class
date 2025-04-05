#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Given data
plaintext = b"This is a top secret."
ciphertext_hex = (
    "c34c12baffcb609d5b63da20d2cbf058"
    "c8e26f3903ab070b99f18d6fbcdfcd19"
)
ciphertext = bytes.fromhex(ciphertext_hex)
iv = b"\x00" * 16

def try_key(word):
    # Pad the English word with spaces to create a 16-byte key
    key = word.ljust(16).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted = cipher.decrypt(ciphertext)
        # Remove PKCS#7 padding
        decrypted = unpad(decrypted, 16)
        if decrypted == plaintext:
            return True
    except Exception:
        return False
    return False

# Open the dictionary file provided (words.txt)
with open("words.txt", "r") as file:
    for line in file:
        word = line.strip()
        if len(word) < 16:  # Only consider words that are less than 16 characters
            if try_key(word):
                print("Key found:", word)
                break

