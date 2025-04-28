import os, hashlib

def store_password(password: str, iterations: int = 200_000):
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        iterations,
        dklen=32
    )
    return salt.hex(), iterations, dk.hex()

def verify_password(stored_salt_hex, stored_iter, stored_hash_hex, attempt: str):
    salt = bytes.fromhex(stored_salt_hex)
    dk = hashlib.pbkdf2_hmac(
        'sha256',
        attempt.encode(),
        salt,
        stored_iter,
        dklen=32
    )
    return dk.hex() == stored_hash_hex

# Demo
if __name__ == "__main__":
    pwd = "My$ecureP@ssw0rd"
    salt_h, iters_h, hash_h = store_password(pwd)
    print("DB fields:")
    print(" salt:", salt_h)
    print(" iters:", iters_h)
    print(" hash:", hash_h)

    # Verification attempt
    good = verify_password(salt_h, iters_h, hash_h, "My$ecureP@ssw0rd")
    bad  = verify_password(salt_h, iters_h, hash_h, "wrongpass")
    print("Correct login?", good)
    print("Wrong login?", bad)

