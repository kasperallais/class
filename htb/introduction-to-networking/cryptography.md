Cryptography
- Encryption is used on the Internet to transmit data, such as payment information, e-mails, or personal data, confidentially and protected against manipulation
- Data is encrypted using various cryptographic algorithms based on mathematical operations
- With the help of encryption, data can be transformed into a form that unauthorized persons can no longer read
- Digital keys in symmetric or asymmetric encryption processes are used for encryption
- It is easier to crack cipher texts or keys depending on the encryption methods used
- If state-of-the-art cryptographic methods with extensive key lengths are used, they work very securely an dare almost impossible to compromise for the time being
- Asymmetric methods have only been known for a few decades
Symmetric Encryption
- Symmetric encryption, also known as secret key encryption, is a method that uses the same key to encrypt and decrypt the data
- This means the sender and the receiver must have the same key to decrypt the data correctly
- If the secret key is shared or lost, the security of the data is no longer guaranteed
- Critical actions for symmetric key encryption methods represent the distribution, storage, and exchange of the keys
- Advanced Encryption Standard (AES) and Data Encryption Standard (DES) are examples of symmetric encryption algorithms
- This type of encryption is often used to encrypt large amounts of data, such as files on a hard drive or data sent over the network
- AES is considered to be the most secure encryption nowadays
Asymmetric Encryption
- Asymmetric encryption, also known as public-key encryption, is a method of encryption that uses two different keys:
    - A public key
    - A private key
- The public key is used to encrypt the data, while the private key is used to decrypt the data
- This means anyone can use a public key to encrypt the data for someone, but only the recipient with the associated private key can decrypt the data
- Examples of asymmetric encryption methods include RSA, PGP, and ECC
Public-Key Encryption
- One advantage of asymmetric encryption is its security
- Since the security is based on very hard-to-solve mathematical problems, simple attacks cannot crack it
- Furthermore, the issue of the key exchange is bypassed
- This is a significant problem with symmetric encryption methods
- However, since the public key can be accessible to everyone, there is no need to exchange keys secretly
- In addition, the asymmetric methods open up the possibility of authentication with digital signatures
Data Encryption Standard
- DES is a symmetric-key block cipher, and its encryption works as a combination of the one-time pad, permutation, and substitution ciphers applied to bit sequences
- It use the same key in both encrypting and decrypting data
- They key consists of 64 bits, with 8 bits used as a checksum
- Therefore, the actual key length of DES is only 56 bits
- That is why one always speaks of a key length of 56 bits when referring to DES
- To prevent the danger form frequency analysis, not single letters, but each 64-bit block of plain text is encrypted to a 64-bit block of ciphertext
- An extension of DES is so-called Triple DES / 3DES, which encrypts data more securely
- The procedure for this usually consists of three keys, with the first key being used to encrypt the data, the second to decrypt the data, and the third to encrypt the data again
- 3DES was considered more secure than the original DES because it provides greater security using three rounds of encryption, although using a 56-bit key still limits it
- AES, the successor to DES, provides higher security using longer key lengths and is not the most widely used symmetric encryption technology
Advanced Encryption Standard
- Compared to DES, AES uses 128-bit (AES-128), 192-bit (AES-192), or 256-bit (AES-256) keys to encrypt and decrypt data
- In addition, AES is faster than DES because it has a more efficient algorithm structure
- This is because it can be applied to multiple data blocks at once, making it faster
- This means that AES encryption and decryption can be performed faster than DES, which is especially important when large amounts of data need to be encrypted
Cipher Modes
- A cipher mode refers to how a block cipher algorithm encrypts a plain text message
- A block cipher algorithm encrypts data, each using fixed-size blocks of data
- A cipher mode defines how these block are processed and combined to encrypt a message of any length
- Each mode has its characteristics and is more suitable for certain use cases
- The choice of encryption mode depends on the application's requirements and the security objectives to be achieved
