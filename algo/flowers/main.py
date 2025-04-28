import time
import random
import pandas as pd
import matplotlib.pyplot as plt

# ---- Part 1: Naïve recursive solution ----
def max_beauty_recursive(flowers, i, j):
    if i == j:
        return flowers[i]
    total = sum(flowers[i:j+1])
    left = max_beauty_recursive(flowers, i+1, j)
    right = max_beauty_recursive(flowers, i, j-1)
    return total - min(left, right)

# ---- Part 2: Bottom-up DP solution ----
def max_beauty_dp(flowers):
    n = len(flowers)
    # prefix sums for O(1) range‐sum queries
    prefix = [0]*(n+1)
    for k in range(1, n+1):
        prefix[k] = prefix[k-1] + flowers[k-1]
    def total(a, b):
        return prefix[b+1] - prefix[a]

    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = flowers[i]
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            dp[i][j] = total(i, j) - min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

# ---- Timing the recursive version ----
rec_ns = [2, 4, 6, 8, 10, 12, 14, 16, 18]
rec_times = []
for n in rec_ns:
    arr = [random.randint(1, 1000) for _ in range(n)]
    t0 = time.perf_counter()
    max_beauty_recursive(arr, 0, n-1)
    rec_times.append(time.perf_counter() - t0)

rec_df = pd.DataFrame({'n': rec_ns, 'time_sec': rec_times})
print("Naïve Recursive Runtimes:")
print(rec_df.to_string(index=False))

plt.figure()
plt.plot(rec_df['n'], rec_df['time_sec'], marker='o')
plt.title('Naïve Recursive Runtime vs n')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()

# ---- Timing the DP version ----
dp_ns = [100, 200, 400, 800, 1600, 3200, 6400]
dp_times = []
for n in dp_ns:
    arr = [random.randint(1, 1000) for _ in range(n)]
    t0 = time.perf_counter()
    max_beauty_dp(arr)
    dp_times.append(time.perf_counter() - t0)

dp_df = pd.DataFrame({'n': dp_ns, 'time_sec': dp_times})
print("\nBottom-up DP Runtimes:")
print(dp_df.to_string(index=False))

plt.figure()
plt.plot(dp_df['n'], dp_df['time_sec'], marker='o')
plt.title('Bottom-up DP Runtime vs n')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()

