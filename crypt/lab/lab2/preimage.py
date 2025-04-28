from Crypto.Hash import SHA256
import struct
import time

def find_preimage(target_prefix: bytes):
    trials = 0
    start = time.perf_counter()
    while True:
        # simple counter input: 4‑byte big‑endian
        b = struct.pack(">I", trials)
        h = SHA256.new(b).digest()
        trials += 1
        if h[:3] == target_prefix:
            return b, trials, time.perf_counter() - start

if __name__ == "__main__":
    import os
    # Run 10 experiments, each with a random 3‑byte target
    results = []
    for run in range(1, 11):
        tgt = os.urandom(3)
        _, t, _ = find_preimage(tgt)
        print(f"Run {run:2d}: {t:,} trials")
        results.append(t)
    avg = sum(results) / len(results)
    print(f"\nAverage trials: {avg:,.0f}")

