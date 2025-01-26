# Modern Block Ciphers
- Now look at modern symmetric block ciphers
- One of the most widely used types of cryptographic algorithms
- Provide confidentiality/authentication services
- Focus on DES (Data Encryption Standard)

# Block vs. Stream Ciphers
- Stream ciphers process messages a bit or byte at a time when en/decrypting
- Block ciphers process messages in blocks, each of which is then en/decrypted

# Block Cipher and the Feistel Cipher Structure
- Most symmetric block ciphers are based on a Feistel Cipher Structure
- Horst Feistel was a cryptographer who worked on the design of ciphers at IBM, initiating research that would cumulate in the development of the Data Encryption Standard in the 1970s

# Motivation for the Feistel Cipher Structure
- Block Cipher:
    - n bits plaintext -> n bits ciphertext
    - 2^n possible plaintext blocks
- Reversible (non-singular) transformation
    - Each unique plaintext block -> a unique ciphertext block
    - 2^n! reversible transformations
- Feistel refers to an n-bit general substitution as an ideal block cipher
    - Allows for the maximum number of possible encryption mappings from the plaintext to ciphertext block

# The Problems of Idea Block Cipher
- The block size n must be very large to thwart attacks
    - Statistical analysis of block content, due to small block size
- Straightforward mappings are not practical from an implementation and performance point of view
    - In general, key length = n*2^n bits
    - For a 64-bit block, key length = 64 * 2^64 = 2^70
- Poorly confined mappings (to a subset of 2^n! reversible transformations) may be vulnerable to cryptanalysis

# Feistel's Observation
- What is needed is an approximation to the ideal block cipher system for large n, built up out of components that are easily readable

# The Feistel Cipher
- Approximate the idea block cipher using a product cipher
    - The execution of two or more simple cipher in sequence
    - The final result or product is cryptographically stronger than any of the components cipher
- The essence of the approach
    - Key length k bits, block length n bits, 2^k instead of 2^n!
    - Alternate substitutions and permutations to defend against cryptanalytic attacks
    - A practical application of the Claude Shannon's proposal

# Claude Shannon and Substitution-Permutation Ciphers
- Claude Shannon introduced idea of substitution-permutation (S-P) networks in a 1949 paper
    - Form basis of modern block ciphers
- S-P nets are based on the two primitive cryptographic operations
    - Substitution (S-box)
    - Permutation (P-box)
- Provide confusion & diffusion of message and key
- Thwart cryptanalysis based on statistical analysis

# Confusion and Diffusion
- Cipher aims to completely obscure statistical properties of original message
- More practically, combining S&P elements to obtain:
    - Diffusion - make the statistical relationship between plaintext and ciphertext as complex as possible
        - Achieved by repeated permutation followed by a function
        - Having each ciphertext digit be affected by many plaintext digits
    - Confusion - make the statistical relationship between ciphertext and key as complex as possible
        - Achieved by complex substitution

# Feistel Cipher Structure
- Horst Feistel devised the Feistel cipher
    - Based on concept of invertible product cipher
- Partition input block into two halves
    - Process through multiple rounds which
    - Perform a substitution on left half data based on round function of right half & subkey
    - Then have permutation swapping halves
- Implement Shannon's S-P net concept
