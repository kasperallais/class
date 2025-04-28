import secrets
import binascii

from Crypto.Cipher import AES

aes_128_key_bytes = secrets.token_bytes(16)
print("AES Key (hex):", binascii.hexlify(aes_128_key_bytes))
