# Classical Substitution Ciphers
- Where letters of plaintext are replaced by other letters or by numbers or symbols
- Or if plaintext is viewed as a sequence of bits, then substitution involves replacing plaintext bit patterns with ciphertext bit patterns

# Caesar Cipher
- Earliest known substitution cipher
- First attested use in military affairs
- Replaces each letter with the letter 3 places further down the alphabet
- Hard-coded key
- General form of Caesar cipher:
    - c = E(k,p) = (p+k) mod (26)
    - p = D(k,c) = (c-k) mod (26)
- Key is 1 letter long

# Cryptanalysis of Caesar Cipher
- Encryption and decryption algorithms are known
- Only have 26 possible keys
    - A maps to A,B,...,Z
    - A brute force search, could simply try each in turn
    - Do need to recognize when we have plaintext
    - eg. break ciphertext 'GCUA VQ DTGCM'
- Language of the plaintext is known and easily recognizable

# Monoalphabetic Cipher
- Rather than just shifting the alphabet
- Could shuffle (jumble) the letters arbitrarily
- Each plaintext letter maps to a different random ciphertext letter
- Key is 26 letters long

# Monoalphabetic Cipher Security
- Now we have a total of 26! = 4 * 10^26 keys
    - Permutation
    - Key Space: 10 orders of magnitude greater than DES
- With so many keys, might think it is secure but would be WRONG
- Problem is language characteristics

# Language Redundancy and Cryptanalysis
- Human languages are redundant
- Letters are not equally commonly used
- In English, E is by far the most common letter
- Other letters like Z,J,K,Q,X are fairly rare

# More on Frequencies
- Also useful are frequencies of common two-letter combinations, known as digrams, and three-letter combinations, known as trigrams
- Common libraries exist for single, double, triple, etc. occurrences in a particular language

# Use in Cryptanalysis
- Key concept - Monoalphabetic substitution ciphers do not change relative letter frequencies
- Discovered by Arabian scientists in 9th century
- Calculate letter frequencies for ciphertext
- Compare counts/plots against known values
- For monoalphabetic must identify each letter
    - tables of common double/triple letters help
    - The most frequent trigram is "the"

# Playfair Cipher
- Not even the large number of keys in a monoalphabetic cipher provides security
- One approach to improving security was to encrypt multiple letters
- The Playfair Cipher is an example

# Playfair Key Matrix
- A 5x5 matrix of letters based on a keyword
- Fill in letters of keyword
- Fill rest of matrix with other letters

# Encrypting and Decrypting
- Plaintext is encrypted two letters at a time
    - If a pair is a repeated letter, insert filler like 'x'
    - If both letters fall in the same row, replace each with the letter to the right
    - If both letters fall in the same column, replace each with the letter below it
    - Otherwise each letter is replaced by the letter in the same row and in the same column of the other letter pair

# Hill Cipher
- Developed by mathematician Lester Hill in 1929
- The encryption algorithm takes m successive plaintext letters and substitutes for them m ciphertext letters
- The substitution is determined by m linear equations in which each character is assigned a numerical value

# Relative Frequency of Occurrence of Letters
- Playfair cipher has a flatter distribution than does plaintext, but nevertheless it reveals plenty of structure for a cryptanalyst to work with.

# Security of Hill Cipher
- As with Playfair, the strength of the Hill cipher is that it can hide single-letter frequency information
- The use of larger matrix hides more frequency information
- A 3x3 Hill Cipher hides not only single-letter but also two-letter frequency information
- Although the Hill cipher is strong against a ciphertext-only attack, it is easily broken with a know plaintext cipher

# Polyalphabetic Ciphers
- Improve security using multiple monoalphabetic ciphers
- Make cryptanalysis harder with more alphabets to guess and flatter frequency distribution
- Use a key to select which alphabet is used for each letter of the message
- Use each alphabet in turn
- Repeat from start after end of key is reached

# Vigenere Cipher
- Simplest polyalphabetic substitution cipher
- Effectively multiple Caesar ciphers
- Key is multiple letters long K=k_0k_1...k_(m-1)
- ith letter specifies ith alphabet to use
- Use each alphabet in turn, repeat after m letters
- Encryption: C_i = (P_i+k_(imodm) mod 26
- Decryption: P_i = (C_i-k_(imodm) mod 26

# Security of Vigenere Ciphers
- Have multiple ciphertext letter for each plaintext
- Letter frequencies are obscured but not totally lost
- The Kasiski method for attacking Vigenere Ciphers

# Autokey Cipher
- Ideally want a key as long as the message
- Vigenere proposed the autokey cipher with keyword prefixed to message as a running key
- Knowing keyword can recover the first few letters
- Use these in turn on the rest of the message but still have frequency characteristics to attack
    - Key & plaintext share the same frequency distribution of letters

# Vernam Cipher 
- Ultimate defense is to use a key as long as the plaintext with no statistical relationship to it
- Invented by AT&T engineer Gilbert Vernam in 1918
- Originally proposed using a very long but eventually repeating key
- Encrypt binary data rather than letters
- XOR operation
- Can still be broken: sufficient ciphertext, known plaintext

# One-Time Pad
- If a truly random key as long as the message is used, the cipher will be secure
- Called a One-Time pad
- Is unbreakable since ciphertext bears no statistical relationship to the plaintext
- Since for any plaintext & any ciphertext there exists a key mapping one to the other
- Can only use the key once though

# One-Time Pad Analysis
- In theory, we need look no further for a cipher
- The one-time pad offers unconditional security but, in practice, has two fundamental difficulties
    - There is the practical problem of making large quantities of random keys
    - Even more daunting is the problem of key distribution and protection
- The one-time pad is of limited utility, and is useful primarily for low-bandwidth channels requiring very high security

# Transposition Ciphers
- Now consider classical transposition or permutation ciphers
- These hide the message by rearranging the letter order
- Without altering the actual letters used
- Can recognize these since they have the same frequency distribution as the original text

# Rail Fence Cipher
- Write message letters out diagonally over a number of rows
- Then read off cipher row by row

# Row Transposition Ciphers
- Is a more complex transposition
- Write the message in a rectangle, row by row, and read the message off shuffling the order of the columns in each row
- The order of the columns is the key

# Security of Transposition Ciphers
- A pure transposition cipher is easily recognized
    - Letter frequencies do not change
    - Digram and trigram frequency tables can be useful
- Can be made significantly more secure by performing multiple states of transposition

# Product Ciphers
- Ciphers using single substitution or transposition are not secure because of language characteristics
- Hence consider using several ciphers in succession to make harder, but:
    - Two substitution make a more complex substitution
    - Two transpositions make a more complex transposition
    - But a substitution followed by a transposition makes a new much harder cipher
- This is the bridge from classical to modern ciphers

# Rotor Machines
- Before modern ciphers, rotor machines were most common complex ciphers in use
- Widely used in WW2
- Implemented a very complex, varying substitution cipher
- Used a series of cylinders, each giving one substitution which rotated and changed after each letter was encrypted
- With 3 cylinders have 26^3 = 17576 alphabets before the system repeats

# Steganography
- Hides existence of message
    - Using only a subset of letters/words in a longer message marked in some way
    - Using invisible ink
    - Hiding in LSB in graphic image or sound file
- Has drawbacks
    - High overhead to hide relatively few info bits
    - Advantage is can obscure encryption use
