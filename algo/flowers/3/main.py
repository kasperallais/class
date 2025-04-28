def max_beauty_dp_with_traceback(flowers):
    n = len(flowers)
    # Precompute prefix sums
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + flowers[i - 1]
    
    # Get sum of interval [i.j]
    def total(i, j):
        return prefix[j + 1] - prefix[i]
    
    # Create dp and parent tables
    # dp[i][j] will hold the maximum beauty the current player can secure from the subarray flowers[i...j]
    # parent[i][j] will record the optimal decision: 'L' if picking the left flower, 'R' if picking the right flower (with ties broken in favor of 'L')
    dp = [[0] * n for _ in range(n)]
    parent = [[''] * n for _ in range(n)]
    
    # Base cases: one flower
    for i in range(n):
        dp[i][i] = flowers[i]
        parent[i][i] = 'L'
    
    # Fill the dp table for subproblems with more than one flower
    # L is the length of the interval
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            # Calculate the score if the current player picks left or right
            left_choice = total(i, j) - dp[i + 1][j]
            right_choice = total(i, j) - dp[i][j - 1]
            
            # Choose the optimal move and record the parent's pointer
            if left_choice >= right_choice: 
                dp[i][j] = left_choice
                parent[i][j] = 'L'
            else:
                dp[i][j] = right_choice
                parent[i][j] = 'R'
    
    # Traceback step
    moves = []
    i, j = 0, n - 1
    # current_turn: 0 for your turn, 1 for rival
    current_turn = 0
    while i <= j:
        # Base-case: Only one flower left
        if i == j:
            moves.append(i + 1)
            break
        # Use the parent pointer computed for the current subproblem
        if parent[i][j] == 'L':
            moves.append(i + 1) 
            i += 1
        else:
            moves.append(j + 1)
            j -= 1
        current_turn = 1 - current_turn
    
    return dp[0][n - 1], moves

# Read input.
n = int(input().strip())
flowers = list(map(int, input().split()))

# Compute the result and the sequence of moves
max_beauty, order = max_beauty_dp_with_traceback(flowers)

print(max_beauty)
print(" ".join(map(str, order)))
