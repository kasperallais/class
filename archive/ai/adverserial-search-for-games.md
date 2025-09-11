# Games vs. Search Problems
- "Unpredictable" opponents - solution is a policy
    - Specify a move for every opponent response
    - Time limits - cannot search entire tree, must approximate

# Types of Games
- Many different kinds of games!
- Axes:
    - Deterministic or stochastic?
    - One, two, or more players?
    - Zero sum?
    - Perfect information
- Want algorithms for calculating a strategy which recommends a move from each state

# Deterministic Games
- Many possible formalizations, one is:
    - States: S (start at s_0)
    - Players: P={1...N}
    - Actions: A
- Solution for a player is a policy: S -> A

# Zero-Sum Games
- General Games
    - Agents have independent utilities
    - Cooperation, indifference, competition, and more are all possible
    - More later on zero-sum games
- Zero-Sum Games
    - Agents have opposite utilities
    - Lets us think of a single value that one maximizes and the other minimizes
    - Adversarial, pure competition

# Value of a State
- Value of a state: The best achievable outcome from that state

# Adversarial Search (Minimax)
- Deterministic, zero-sum games:
    - Tic-tac-toe, chess, checkers
    - One player maximizes result
    - The other minimizes result
- Minimax search:
    - A state-space search tree
    - Players alternate turns
    - Compute each node's minimax value: the best achievable utility against a rational adversary

# Minimax

def value(state):
    if the state is a terminal state: return the state’s utility
    if the next agent is MAX: return max-value(state)
    if the next agent is MIN: return min-value(state)

def max-value(state):
    initialize v = -∞
    for each successor of state:
        v = max(v, value(successor))
    return v

def min-value(state):
    initialize v = +∞
    for each successor of state:
        v = min(v, value(successor))
    return v

# Minimax Efficiency
- How efficient is minimax?
    - Just like DFS
    - Time: O(b^m)
    - Space: O(bm)

# Resource Limits
- Problem: In realistic games, cannot search to leaves!
- Solution: Depth-limited search
    - Instead, search only to a limited depth in the three
    - Replace terminal utilities with an evaluation function for non-terminal postilions
- Guarantee of optimal play is gone
- More plies makes a BIG difference
- Use iterative deepening for an anytime algorithm

# Depth Matters
- Evaluation functions are always imperfect
- The deeper in the tree the evaluation function is buried, the less the quality of the evaluation function matters
- An important example of the trade-off between complexity of features and complexity of computation
