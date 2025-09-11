# Properties of Decision Problems`
- Determinism
    - Deterministic: Single outcome for every action
    - Non-deterministic: Multiple (random) outcomes for an action
- Observability
    - Fully: State is known at all times (path planning)
    - Partially: State is uncertain; learn through observations
    - Non-observable: Unknown state; single solution for all cases
- Solution to non-deterministic or partially-observable problems are policies (not sequences)

# Depth-First Search
- Strategy: Expand a deepest node first
- Implementation: Fringe is a LIFO stack

# Properties of Search Algorithms
- Properties of search algorithms
    - Completeness: Does it always find a solution if one exists?
    - Time complexity: Total number of nodes generated/expanded
    - Space complexity: Maximum number of nodes in memory
    - Optimality: Does it always return a least-cost solution?
- Parameters for time/space analysis
    - b: maximum branching factor
    - d: depth of least-cost solution
    - m: maximum depth of search tree (may be inf)

# DFS Properties
- What nodes does DFS expand?
    - Some left prefix of the tree
    - Could process the whole tree
    - Time complexity: If m is finite, O(b^m)
- How much space does the fringe take?
    - Only has siblings on path to root, so O(bm)
- Is it complete?
    - No: m could be infinite
    - Complete if finite space, modified to detect cycles
- Is it optimal?
    - No, it finds the "leftmost" solution, regardless of depth or cost

# Breadth-First Search
- Strategy: Expand a shallowest node first
- Implementation: Fringe is a FIFO queue

# BFS Properties
- What nodes does BFS expand?
    - Processes all nodes above the shallowest solution
    - Let depth of shallowest solution be s
    - Search takes time O(b^s)
- How much space does the fringe take?
    - Has roughly the last tier, so O(b^s)
- Is it complete?
    - s must be finite if the solution exists, so yes!
- Is it optimal?
    - Only if costs are all 1
