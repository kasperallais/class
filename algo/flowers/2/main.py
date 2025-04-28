def max_beauty_dp(flowers):
    n = len(flowers)
    # Precompute prefix sums
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + flowers[i - 1]
    
    # Get sum of interval [i, j]
    def total(i, j):
        return prefix[j + 1] - prefix[i]
    
    # Initialize DP table
    dp = [[0] * n for _ in range(n)]
    
    # Base cases: one flower intervals
    for i in range(n):
        dp[i][i] = flowers[i]
    
    # Build the table for intervals of increasing lengths
    # L is the length of the interval
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            # Recurrence relation: total beauty from i to j minus the best the opponent can obtain
            dp[i][j] = total(i, j) - min(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n - 1]

# Read input
n = int(input().strip())
flowers = list(map(int, input().split()))

# Compute the maximum beauty score of your bouquet
result = max_beauty_dp(flowers)
print(result)

