# Symmetric Encryption
- Conventional / Secret-Key / Single-Key
- Sender and Recipient share a common key
- All classical encryption algorithms are secret-key
- Was the only type prior to invention of public-key in 1970's

# Requirements
- Two requirements for secure use of symmetric encryption:
    - A strong encryption algorithm
    - A secret key known only to sender / receiver
- Mathematically have: 
    - Y = E(K,X)
    - X = D(K,Y)
- Assume en(de)cryption algorithm is known
- Implies a secure channel to distribute key

# Cryptography
- Can characterize cryptographic systems by:
    - Type of encryption operations used:
        - Substitution 
        - Transposition
        - Multiple stages of substitutions and transpositions
    - Number of keys used
        - Single-key or secret-key
        - Two-key or public
    - Way in which plaintext is processed
        - Block
        - Stream

# Attacks to Cryptographic Systems
- Objective to recover key not just message
- Two general approaches:
    - Cryptanalytic attack
        - Characteristics of the algorithm
    - Brute-force attack
        - Key space
- If either succeed all key use compromised

# Cryptanalytic Attacks
- Ciphertext only
    - Only know algorithm & ciphertext
- Known plaintext
    - Know some plaintext/ciphertext pairs
- Chosen plaintext
    - Select plaintext and obtain ciphertext
- Chosen ciphertext
    - Select ciphertext and obtain plaintext
- Chosen text
    - Select plaintext or ciphertext to en/decrypt

# More Definitions
- Unconditional Security
    - No matter how much computer power or time is available, the cipher cannot be broken since the ciphertext provides insufficient information to uniquely determine the corresponding plaintext
        - One-time pad
- Computational Security
    - Given limited computing resources, the cipher cannot be broken

# Brute Force Search
- Always possible to simply try every key
- Most basic attack, proportional to key size
    - On average, half of the key space must be tried
- Assume either know/recognize plaintext

