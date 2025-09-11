# Uninformed Search
- Uninformed - Use only information in problem definition
- Informed - Uses additional problem structure

# Iterative Deepening
- Idea: Get DFS's space advantage with BFS's time/shallow-solution advantages
    - Run a DFS with depth limit 1. If no solution ...
    - Run a DFS with depth limit 2. If no solution ...
    - Run a DFS with depth limit 3. ...
- Most work happens in the deepest level searched

# Properties of Iterative Deepening Search
- How many does does Iterative Deepening expand?
    - DFS with limit l costs O(b^l)
    - Repeats DFS until finding a solution
    - (d+1)b^0 + db^1 + (d-1)b^2 + ... + b^d = O(b^d)
- How much space does the fringe take?
    - Linear memory up to least cost solution at depth d
    - Total memory O(bd)
- Is it complete?
    - Yes
- Is it optimal
    - Only if step cost is 1 
    - Can use cost limits instead of depth limits

# A Warning about Implementation
- Compare naive implementations
    - Iterative deepening (IDS) vs Breadth-First (BFS)
- How many nodes get expanded?
    - Consider b=10 and d=5 & solution at far right leaf
    - N(IDS) = 50 + 400 + 3,000 + 20000 + 100000 = 123,450
    - N(BFS) = 10 + 100 + 1,000 + 10,000 + 100,000 + 999,990 = 1,111,100
- Why can this happen
    - IDS does better by not expanding nodes at depth d
    - Fix: Modify implementation of BFS to test for goals when nodes generated

# Cost-Sensitive Search
- BFS finds the shortest path in terms of number of actions
- It does not find the least-cost path

# Repeated States
- Failure to detect repeated states can turn linear problems exponential

# Graph Search
- Check for repeated nodes if your graph doesn't look like a tree

# Uniform Cost Search
- Strategy: Expand a cheapest node first
- Fringe is a priority queue

# Uniform Cost Search (UCS) Properties
- What nodes does UCS expand?
    - Process all nodes with cost less than cheapest solution!
    - If that solution costs C* and arcs cost at east epsilon, then the "effective depth" is roughly C*/epsilon
- How much space does the fringe take?
    - Dominated by effective depth O(B^(C*/epsilon)
- Is it complete
    - Assuming best solution has a finite cost and minimum arc cost is positive, yes
- Is it optimal
    - Yes, nodes expanded in increasing order of path cost

# Uninformed Algorithms
- Uninformed: Use only information in problem definition
    - Breadth-first search
    - Depth-first search
    - Iterative deepening search
    - Uniform-cost search

# Some Common "Gotchas"
- Graph vs. tree search: b^d can be much larger than E+V
- Uniform-cost search may expand may small edges
- The difference between b^d and b^(d+1) can be large
