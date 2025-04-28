def max_beauty(flowers, i, j):
    # When there's only one flower
    if i == j:
        return flowers[i]
    
    # Calculate the total beauty score from index i to j
    total = sum(flowers[i:j+1])
    
    # Recursively calculate the opponent's best outcomes for both choices
    score_if_left_taken = max_beauty(flowers, i + 1, j)
    score_if_right_taken = max_beauty(flowers, i, j - 1)
    
    # Net score is total minus opponent's best
    return total - min(score_if_left_taken, score_if_right_taken)

# Read input values
n = int(input().strip())
flowers = list(map(int, input().strip().split()))

# Compute the maximum beauty score of bouquet
result = max_beauty(flowers, 0, n - 1)
print(result)

