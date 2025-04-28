import os
import time
import hashlib

def derive_key_pbkdf2(password: str, iterations: int = 1000, salt: bytes = None):
    # Generate Salt
    if salt is None:
        salt = os.urandom(16)

    # Derive key
    start = time.perf_counter()
    key = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=password.encode('utf-8'),
        salt=salt,
        iterations=iterations,
        dklen=16
    )
    elapsed = time.perf_counter() - start

    # Return salt, key, and time taken
    return salt, key, elapsed

# Demo and evaluation
password = "ThisIsASecurePwd!"
salt, key, elapsed = derive_key_pbkdf2(password, iterations=1000)

print(f"Salt (hex):       {salt.hex()}")
print(f"Key   (hex):      {key.hex()}")
print(f"Elapsed time:     {elapsed:.4f} seconds")


_, _, t1 = derive_key_pbkdf2(password, iterations=1000)

est_max_iters = int(1000 / t1)

_, _, t2 = derive_key_pbkdf2(password, iterations=est_max_iters)

print(f"{est_max_iters} iters took {t2:.4f}s")

