# Depth of Game Trees
- One 'ply' is one turn for one player

# Alpha-Beta Pruning
- General Configuration (MIN Version)
    - Computing the Min-Value at some node n
        - looping over n's children
        - n's estimate of the children's min dropping from +∞
    - Who cares about n's value? MAX
        - Let a be the best value that MAX can get at any choice point along the current path from the root
    - If n becomes worse than a
        - MAX will avoid
        - Stop considering n's other children

# Alpha-Beta Implementation

    def max-value(state, α, β):
        initialize v = -∞
            for each successor of state:
            v = max(v, value(successor, α, β))
            if v ≥ β return v
        α = max(α, v)
        return v

    def min-value(state , α, β):
        initialize v = +∞
        for each successor of state:
            v = min(v, value(successor, α, β))
            if v ≤ α return v
            β = min(β, v)
        return v

# Alpha-Beta Pruning Properties
- This pruning has no effect on minimax value computed for the root
- Values of intermediate nodes might be wrong
    - Children of the root may have the different values
- Good child ordering improves effectiveness of pruning
- With 'perfect ordering'
    - Time complexity drops to O(b^(m/2))
    - Doubles solvable depth
    - Full search of, e.g. chess, is still hopeless
- This is a simple example of meta reasoning (computing about what to compute)

# Evaluation Functions
- Evaluation function score non-terminals in depth-limited search
- Ideal function: returns the actual minimax value of the position
