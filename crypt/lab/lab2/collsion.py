from Crypto.Hash import SHA256
import struct
import time

def find_collision():
    seen = {}
    trials = 0
    start = time.perf_counter()
    while True:
        b = struct.pack(">I", trials)
        prefix = SHA256.new(b).digest()[:3]
        trials += 1
        if prefix in seen:
            return trials, time.perf_counter() - start
        seen[prefix] = b

if __name__ == "__main__":
    results = []
    for run in range(1, 11):
        t, _ = find_collision()
        print(f"Run {run:2d}: {t:,} trials")
        results.append(t)
    avg = sum(results) / len(results)
    print(f"\nAverage trials: {avg:,.0f}")

