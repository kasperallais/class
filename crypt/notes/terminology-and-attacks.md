# Symmetric Key Encryption
- Also called conventional or single-key encryption
- Sender and receiver share one key
- All classical ciphers are symmetric

# Core Terminology
- Plaintext: Original Message
- Ciphertext: Transformed message
- Cipher: Algorithm that maps plaintext to ciphertext
- Key: Secret information used by the cipher
- Encrypt: Convert plaintext into ciphertext
- Decrypt: Recover plaintext from ciphertext
- Cryptography: Study of encryption methods
- Cryptanalysis: Study of breaking ciphertext without the key

# Symmetric-Cipher Model
- Encryption: Y=E(K,X)
- Decryption: X=D(K,Y)
- Security relies on
    - A strong, well designed algorithm
    - A key kept secret between sender and receiver
- Assumes adversary knows the algorithm
- Requires a secure channel for key distribution

# Classification of Classical Ciphers
- By operation:
    - Substitution
    - Transposition
    - Combinations
- By key usage:
    - Single-key (symmetric)
    - Two key (public-key)

# Attack Models
- Cryptanalytic attacks
    - Ciphertext-only
    - Known Plaintext
    - Chosen Plaintext
    - Chosen Ciphertext

